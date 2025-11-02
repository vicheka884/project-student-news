# 🎓 Student News Blog Website

A modern, full-featured blog website for student news built with Flask and styled with Tailwind CSS.

## ✨ Features

### For Students (Regular Users)
- 📝 **Create Posts**: Share news, events, and announcements
- 💬 **Comment**: Engage in discussions on posts
- 🔄 **Share**: Share posts with the community
- 👤 **Profile**: View your posts, comments, and activity
- 🏷️ **Categories**: Browse news by category (Academic, Sports, Events, Clubs, Announcements, Other)

### For Administrators
- 🛡️ **Admin Dashboard**: Comprehensive view of all site activity
- 👥 **User Management**: View and manage all users
- 📊 **Statistics**: Track total users, posts, comments, and shares
- 🗑️ **Content Moderation**: Delete inappropriate posts and comments
- 👮 **Full Control**: Access to all site features and data

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   python app.py
   ```

3. **Access the website**
   - Open your browser and navigate to: `http://127.0.0.1:5000`
   - The database will be created automatically on first run

### Default Admin Account
- **Username**: `admin`
- **Password**: `admin123`
- **Note**: Change this password after first login for security!

## 📁 Project Structure

```
student-news/
├── app.py                 # Main Flask application
├── models.py              # Database models (User, Post, Comment, Share)
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html         # Base template with navbar and footer
│   ├── index.html        # Homepage
│   ├── news.html         # All news posts page
│   ├── post.html         # Single post view
│   ├── create_post.html  # Create new post
│   ├── edit_post.html    # Edit existing post
│   ├── profile.html      # User profile page
│   ├── admin.html        # Admin dashboard
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── 403.html          # Forbidden error page
│   └── 404.html          # Not found error page
└── student_news.db       # SQLite database (created automatically)
```

## 🎨 Features Overview

### User Authentication
- Secure registration and login system
- Password hashing with Werkzeug
- Session management with Flask-Login
- Role-based access control (Admin vs Student)

### Post Management
- Create, read, update, and delete posts
- Category-based organization
- Rich text content support
- Author attribution
- Timestamps for creation and updates

### Engagement Features
- **Comments**: Threaded discussions on posts
- **Shares**: Share posts with the community
- **User Profiles**: View user activity and contributions

### Admin Controls
- Complete user management
- Content moderation tools
- Site-wide statistics dashboard
- Bulk actions support

## 🎯 Usage Guide

### For Students

1. **Register an Account**
   - Click "Register" in the navbar
   - Fill in your username, email, and password
   - Click "Create Account"

2. **Create a Post**
   - Log in to your account
   - Click "Create Post" in the navbar
   - Enter title, select category, and write content
   - Click "Publish Post"

3. **Engage with Content**
   - Browse posts on the News page
   - Click on a post to view full details
   - Leave comments to join discussions
   - Share posts you find interesting

### For Admins

1. **Access Admin Dashboard**
   - Log in with admin credentials
   - Click "Admin" in the navbar
   - View comprehensive site statistics

2. **Manage Users**
   - View all registered users
   - See user activity (posts, comments)
   - Delete users if necessary

3. **Moderate Content**
   - Review all posts and comments
   - Delete inappropriate content
   - Monitor site engagement

## 🛠️ Technology Stack

- **Backend**: Flask 3.0.0
- **Database**: SQLite with Flask-SQLAlchemy
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Frontend**: HTML5, Tailwind CSS 3.0
- **Icons**: Font Awesome 6.4.0
- **Password Security**: Werkzeug

## 🔒 Security Features

- Password hashing using Werkzeug
- CSRF protection with Flask-WTF
- Session management
- Role-based access control
- Input validation and sanitization

## 📊 Database Schema

### User
- id, username, email, password_hash
- is_admin (boolean)
- created_at timestamp
- Relationships: posts, comments, shares

### Post
- id, title, content, category
- author_id (foreign key)
- created_at, updated_at timestamps
- Relationships: author, comments, shares

### Comment
- id, content
- author_id, post_id (foreign keys)
- created_at timestamp
- Relationships: author, post

### Share
- id, user_id, post_id (foreign keys)
- created_at timestamp
- Unique constraint: one share per user per post

## 🎨 Design Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Clean, professional interface with Tailwind CSS
- **Intuitive Navigation**: Easy-to-use navbar and page structure
- **Visual Feedback**: Flash messages for user actions
- **Color Coding**: Category badges and role indicators
- **Icon Support**: Font Awesome icons throughout

## 📝 Future Enhancements

- [ ] Email notifications for comments and shares
- [ ] Search functionality
- [ ] Post likes/reactions
- [ ] Image upload support
- [ ] User avatars
- [ ] Advanced text editor (Markdown/Rich text)
- [ ] Export data functionality
- [ ] API endpoints for mobile app
- [ ] Social media integration
- [ ] Advanced analytics

## 🐛 Troubleshooting

### Database Issues
If you encounter database errors, delete `student_news.db` and restart the application to recreate the database.

### Port Already in Use
If port 5000 is already in use, modify the last line in `app.py`:
```python
app.run(debug=True, port=5001)  # Change to any available port
```

### Missing Dependencies
Ensure all packages are installed:
```bash
pip install -r requirements.txt --upgrade
```

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Support

For issues or questions, please create an issue in the project repository.

---

**Happy Blogging! 🎉**
