from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Post, Comment, Share
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'

# ========================================
# DATABASE CONFIGURATION
# Using SQLite for simplicity
# ========================================
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/student_news'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# File upload configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Helper function to save uploaded file
def save_upload_file(file):
    if file and allowed_file(file.filename):
        # Generate unique filename
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4().hex}.{ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return filename
    return None

# Context processor to make categories available in all templates
@app.context_processor
def inject_categories():
    categories = ['Academic', 'Sports', 'Events', 'Clubs', 'Announcements', 'Other']
    return dict(categories=categories)

# Home route
@app.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).limit(6).all()
    return render_template('index.html', posts=posts)

# News page - shows all posts
@app.route('/news')
def news():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', '')
    
    query = Post.query
    if category:
        query = query.filter_by(category=category)
    
    posts = query.order_by(Post.created_at.desc()).paginate(page=page, per_page=9, error_out=False)
    return render_template('news.html', posts=posts, selected_category=category)

# View single post
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
    return render_template('post.html', post=post, comments=comments)

# Create post
@app.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category')
        
        if not title or not content or not category:
            flash('All fields are required!', 'danger')
            return redirect(url_for('create_post'))
        
        # Handle image upload
        image_filename = None
        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                image_filename = save_upload_file(file)
                if not image_filename:
                    flash('Invalid image file. Allowed formats: PNG, JPG, JPEG, GIF, WEBP', 'danger')
                    return redirect(url_for('create_post'))
        
        post = Post(title=title, content=content, category=category, image_filename=image_filename, author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('view_post', post_id=post.id))
    
    return render_template('create_post.html')

# Edit post
@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    # Only author or admin can edit
    if post.author_id != current_user.id and not current_user.is_admin:
        abort(403)
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.category = request.form.get('category')
        post.updated_at = datetime.utcnow()
        
        # Handle image upload
        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                # Delete old image if exists
                if post.image_filename:
                    old_image_path = os.path.join(app.config['UPLOAD_FOLDER'], post.image_filename)
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
                
                # Save new image
                image_filename = save_upload_file(file)
                if image_filename:
                    post.image_filename = image_filename
                else:
                    flash('Invalid image file. Allowed formats: PNG, JPG, JPEG, GIF, WEBP', 'danger')
                    return redirect(url_for('edit_post', post_id=post.id))
        
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('view_post', post_id=post.id))
    
    return render_template('edit_post.html', post=post)

# Delete post
@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    # Only author or admin can delete
    if post.author_id != current_user.id and not current_user.is_admin:
        abort(403)
    
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('news'))

# Add comment
@app.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form.get('content')
    
    if not content:
        flash('Comment cannot be empty!', 'danger')
        return redirect(url_for('view_post', post_id=post_id))
    
    comment = Comment(content=content, author_id=current_user.id, post_id=post_id)
    db.session.add(comment)
    db.session.commit()
    
    flash('Comment added successfully!', 'success')
    return redirect(url_for('view_post', post_id=post_id))

# Delete comment
@app.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post_id
    
    # Only author or admin can delete
    if comment.author_id != current_user.id and not current_user.is_admin:
        abort(403)
    
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully!', 'success')
    return redirect(url_for('view_post', post_id=post_id))

# Share post
@app.route('/post/<int:post_id>/share', methods=['POST'])
@login_required
def share_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    # Check if already shared
    existing_share = Share.query.filter_by(user_id=current_user.id, post_id=post_id).first()
    if existing_share:
        flash('You already shared this post!', 'info')
        return redirect(url_for('view_post', post_id=post_id))
    
    share = Share(user_id=current_user.id, post_id=post_id)
    db.session.add(share)
    db.session.commit()
    
    flash('Post shared successfully!', 'success')
    return redirect(url_for('view_post', post_id=post_id))

# User profile
@app.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(author_id=user_id).order_by(Post.created_at.desc()).all()
    return render_template('profile.html', user=user, posts=posts)

# Admin dashboard
@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    
    users = User.query.all()
    posts = Post.query.order_by(Post.created_at.desc()).all()
    comments = Comment.query.order_by(Comment.created_at.desc()).all()
    
    stats = {
        'total_users': len(users),
        'total_posts': len(posts),
        'total_comments': len(comments),
        'total_shares': Share.query.count()
    }
    
    return render_template('admin.html', users=users, posts=posts, comments=comments, stats=stats)

# Admin delete user
@app.route('/admin/user/<int:user_id>/delete', methods=['POST'])
@login_required
def admin_delete_user(user_id):
    if not current_user.is_admin:
        abort(403)
    
    user = User.query.get_or_404(user_id)
    
    if user.id == current_user.id:
        flash('You cannot delete yourself!', 'danger')
        return redirect(url_for('admin_dashboard'))
    
    db.session.delete(user)
    db.session.commit()
    flash(f'User {user.username} deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not username or not email or not password:
            flash('All fields are required!', 'danger')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Invalid username or password!', 'danger')
    
    return render_template('login.html')

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# Error handlers
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Create admin user if not exists
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(username='admin', email='admin@studentnews.com', is_admin=True)
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print('Admin user created: username=admin, password=admin123')
    
    app.run(debug=True)
