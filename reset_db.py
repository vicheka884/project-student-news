import os
import time

# Delete old database if it exists
db_path = 'instance/student_news.db'
if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print(f"Deleted old database: {db_path}")
    except Exception as e:
        print(f"Could not delete database: {e}")
        print("Please close any programs using the database and try again.")
        exit(1)

# Create new database with correct schema
from app import app, db
from models import User

with app.app_context():
    db.create_all()
    print("Created new database with updated schema!")
    
    # Create admin user
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', email='admin@studentnews.com', is_admin=True)
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print('Admin user created: username=admin, password=admin123')
    
print("\n✅ Database reset complete!")
print("🚀 Now run: python app.py")
