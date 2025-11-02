"""
Create and populate SQLite database with professional sample data
"""
from app import app, db
from models import User, Post, Comment, Share
from werkzeug.security import generate_password_hash

def create_database():
    """Create all database tables"""
    with app.app_context():
        print("\n" + "="*60)
        print("🗄️  CREATING SQLITE DATABASE")
        print("="*60 + "\n")
        
        # Drop all existing tables and recreate
        print("📋 Creating database tables...")
        db.drop_all()
        db.create_all()
        print("✅ All tables created successfully!\n")
        
        # Insert sample data
        insert_sample_data()

def insert_sample_data():
    """Insert rich sample data for a professional-looking database"""
    print("="*60)
    print("📝 POPULATING WITH PROFESSIONAL DATA")
    print("="*60 + "\n")
    
    # ============= USERS =============
    print("👥 Creating diverse users...")
    
    users_data = [
        {'username': 'admin', 'email': 'admin@studentnews.com', 'password': 'admin123', 'is_admin': True},
        {'username': 'sarah_johnson', 'email': 'sarah.j@student.edu', 'password': 'student123', 'is_admin': False},
        {'username': 'michael_chen', 'email': 'michael.c@student.edu', 'password': 'student123', 'is_admin': False},
        {'username': 'emily_rodriguez', 'email': 'emily.r@student.edu', 'password': 'student123', 'is_admin': False},
        {'username': 'david_kim', 'email': 'david.k@student.edu', 'password': 'student123', 'is_admin': False},
        {'username': 'sophia_patel', 'email': 'sophia.p@student.edu', 'password': 'student123', 'is_admin': False},
        {'username': 'james_williams', 'email': 'james.w@student.edu', 'password': 'student123', 'is_admin': False},
        {'username': 'olivia_brown', 'email': 'olivia.b@student.edu', 'password': 'student123', 'is_admin': False},
        {'username': 'editor_news', 'email': 'editor@studentnews.com', 'password': 'editor123', 'is_admin': True},
    ]
    
    users = []
    for user_data in users_data:
        user = User(
            username=user_data['username'],
            email=user_data['email'],
            password_hash=generate_password_hash(user_data['password']),
            is_admin=user_data['is_admin']
        )
        db.session.add(user)
        users.append(user)
    
    db.session.commit()
    print(f"✅ Created {len(users)} diverse users (2 admins, 7 students)")
    
    # ============= POSTS =============
    print("\n📰 Creating engaging posts...")
    
    posts_data = [
        {
            'title': '🎓 Welcome to Student News Hub!',
            'content': 'Welcome to our brand new Student News platform! This is your one-stop destination for all campus news, events, and updates. Stay connected with your fellow students, share your achievements, and never miss an important announcement. We\'re excited to have you here!',
            'category': 'Announcements',
            'author': users[0]  # admin
        },
        {
            'title': '🏀 Basketball Team Clinches State Championship',
            'content': 'In a thrilling overtime victory, our varsity basketball team secured the state championship title last night! The final score was 78-75 against North Valley High. Senior captain Marcus Thompson scored a career-high 32 points. The team showed incredible determination and teamwork throughout the season. Congratulations to Coach Rodriguez and the entire team! 🏆',
            'category': 'Sports',
            'author': users[1]  # sarah_johnson
        },
        {
            'title': '🔬 Annual Science Fair - Next Wednesday',
            'content': 'Mark your calendars! Our Annual Science Fair is happening next Wednesday, November 6th, in the main gymnasium from 9 AM to 4 PM. Over 150 students will be showcasing their innovative projects ranging from robotics to environmental science. Special guest judges include Dr. Amanda Lewis from MIT and Professor Chen from Stanford University. All students, parents, and faculty are welcome to attend!',
            'category': 'Events',
            'author': users[8]  # editor_news
        },
        {
            'title': '🎭 Drama Club Presents "Romeo & Juliet"',
            'content': 'The Drama Club is proud to announce our fall production of Shakespeare\'s timeless classic "Romeo & Juliet". Performances will be held November 15-17 at 7 PM in the school auditorium. Tickets are $10 for students and $15 for adults, available at the door or through our online portal. Don\'t miss this spectacular performance featuring our talented student actors!',
            'category': 'Arts',
            'author': users[2]  # michael_chen
        },
        {
            'title': '💻 New Computer Lab Opens in West Wing',
            'content': 'Great news for tech enthusiasts! The school has opened a state-of-the-art computer lab in the West Wing. The facility features 40 new workstations with the latest software for coding, graphic design, and video editing. The lab is available to all students during school hours and until 6 PM on weekdays. Special thanks to our IT department and generous donors who made this possible!',
            'category': 'Technology',
            'author': users[3]  # emily_rodriguez
        },
        {
            'title': '🌍 Environmental Club Beach Cleanup Success',
            'content': 'Last Saturday, 75 students from our Environmental Club participated in a beach cleanup at Ocean View Beach. Together, we collected over 300 pounds of trash and recyclables! The event was a huge success and we\'re already planning our next cleanup for December. Thank you to everyone who participated and helped make our beaches cleaner! 🌊♻️',
            'category': 'Community',
            'author': users[4]  # david_kim
        },
        {
            'title': '📚 Library Extended Hours During Finals',
            'content': 'Attention all students: The library will be extending its hours during finals week (December 11-15). We\'ll be open from 7 AM to 10 PM to provide you with a quiet study space. Free coffee and snacks will be available in the study lounge. Librarians will also be available for research assistance. Good luck with your exams!',
            'category': 'Announcements',
            'author': users[8]  # editor_news
        },
        {
            'title': '⚽ Soccer Team Seeks New Players',
            'content': 'Our girls\' soccer team is looking for new players for the spring season! No experience necessary - just bring your enthusiasm and willingness to learn. Tryouts will be held on November 8th and 9th from 3:30-5:00 PM on the main field. All grades welcome. Contact Coach Martinez at athletics@school.edu for more information.',
            'category': 'Sports',
            'author': users[5]  # sophia_patel
        },
        {
            'title': '🎵 Music Department Concert This Friday',
            'content': 'Join us this Friday evening for our Fall Concert featuring the school band, orchestra, and choir! The concert starts at 7 PM in the auditorium. Our talented musicians have been practicing all semester and are excited to share their performances with you. Admission is free, and light refreshments will be served. Bring your family and friends!',
            'category': 'Arts',
            'author': users[6]  # james_williams
        },
        {
            'title': '🍕 New Lunch Menu Options Available',
            'content': 'The cafeteria has introduced exciting new lunch options based on student feedback! Now featuring vegetarian and vegan meals, a fresh salad bar, and international cuisine rotating weekly. This week\'s special: Authentic Mexican street tacos on Tuesday and Thai curry on Thursday. Don\'t forget to fill out the survey to suggest more menu items!',
            'category': 'Campus Life',
            'author': users[7]  # olivia_brown
        },
        {
            'title': '🏆 Debate Team Takes Regional Championship',
            'content': 'Congratulations to our debate team for winning the Regional Debate Championship! Seniors Alex Thompson and Maria Garcia took first place in the policy debate category, while junior Ethan Park secured second place in Lincoln-Douglas debate. The team will advance to the state competition in January. Way to represent our school! 🎤',
            'category': 'Academics',
            'author': users[8]  # editor_news
        },
        {
            'title': '🚗 New Student Parking Rules',
            'content': 'Important update for all students with parking permits: Starting November 1st, new parking regulations will be in effect. Please park only in designated student areas (Lots B and C). Faculty parking (Lot A) is strictly off-limits. Violators will receive warnings and potential permit revocation. Digital permits must be displayed on your dashboard. Visit the office for more details.',
            'category': 'Announcements',
            'author': users[0]  # admin
        },
        {
            'title': '🎨 Student Art Exhibition Opens Next Month',
            'content': 'The Visual Arts department is thrilled to announce our annual Student Art Exhibition opening December 1st! The exhibition will showcase paintings, sculptures, photography, and digital art created by our talented students throughout the semester. Opening reception on December 1st at 6 PM with refreshments. The exhibition runs through December 15th.',
            'category': 'Arts',
            'author': users[2]  # michael_chen
        },
        {
            'title': '🤝 Community Service Day - November 18th',
            'content': 'Save the date for our school-wide Community Service Day on November 18th! Students will participate in various service projects including park beautification, senior center visits, food bank volunteering, and tutoring at elementary schools. This is a great opportunity to give back to our community and earn service hours. Sign-up sheets available in the main office!',
            'category': 'Community',
            'author': users[4]  # david_kim
        },
        {
            'title': '📱 New School Mobile App Launched',
            'content': 'Stay connected on the go with our new school mobile app! Available now on iOS and Android. Features include: real-time announcements, class schedules, grades, cafeteria menu, event calendar, and emergency notifications. Download it today from the App Store or Google Play by searching "Student News Hub". Your login credentials are the same as your student portal.',
            'category': 'Technology',
            'author': users[3]  # emily_rodriguez
        },
    ]
    
    posts = []
    for post_data in posts_data:
        post = Post(
            title=post_data['title'],
            content=post_data['content'],
            category=post_data['category'],
            author=post_data['author']
        )
        db.session.add(post)
        posts.append(post)
    
    db.session.commit()
    print(f"✅ Created {len(posts)} engaging posts across multiple categories")
    
    # ============= COMMENTS =============
    print("\n💬 Adding realistic comments...")
    
    comments_data = [
        # Comments on post 1 (Welcome)
        (0, 1, "Love the new platform! So much easier to stay updated now. 😊"),
        (0, 2, "This is awesome! Great work on the design."),
        (0, 4, "Finally! Been waiting for something like this."),
        
        # Comments on post 2 (Basketball)
        (1, 3, "What an amazing game! So proud of our team! 🏀🔥"),
        (1, 5, "Marcus Thompson is a legend! That final shot was incredible!"),
        (1, 6, "Best game I've ever watched! Congratulations team!"),
        (1, 2, "Coach Rodriguez deserves a lot of credit. Great season!"),
        
        # Comments on post 3 (Science Fair)
        (2, 4, "Can't wait to see all the projects! I'm presenting my robotics project."),
        (2, 3, "Will there be livestream for parents who can't attend?"),
        (2, 7, "I heard there are some really impressive AI projects this year!"),
        
        # Comments on post 4 (Drama)
        (3, 6, "Already got my tickets! The cast is incredible this year."),
        (3, 1, "I'm playing Mercutio! Hope to see everyone there! 🎭"),
        
        # Comments on post 5 (Computer Lab)
        (4, 3, "Finally! The old computers were so slow. This is game-changing."),
        (4, 2, "Perfect timing with the coding competition coming up!"),
        (4, 5, "Can we use it for gaming club meetings?"),
        
        # Comments on post 6 (Beach Cleanup)
        (5, 1, "So proud of everyone who showed up! Great turnout."),
        (5, 7, "Count me in for the next one! This was so rewarding."),
        (5, 4, "Thanks to everyone who helped organize this! 🌊"),
        
        # Comments on post 7 (Library Hours)
        (6, 2, "This is exactly what we needed! Thank you!"),
        (6, 5, "Free coffee during finals? You're the best! ☕"),
        
        # Comments on post 9 (Music Concert)
        (8, 6, "I'll be playing violin in the orchestra! Hope you can make it!"),
        (8, 1, "The choir sounds amazing this year. Don't miss it!"),
        
        # Comments on post 10 (Lunch Menu)
        (9, 7, "Finally some vegan options! Thank you so much! 🌱"),
        (9, 4, "Those tacos were delicious! Best cafeteria food ever!"),
        (9, 3, "Can we get sushi next? That would be amazing!"),
        
        # Comments on post 11 (Debate Team)
        (10, 2, "Congratulations! You all worked so hard for this."),
        (10, 5, "Alex and Maria are unstoppable! Good luck at state!"),
    ]
    
    comments = []
    for post_idx, user_idx, content in comments_data:
        comment = Comment(
            content=content,
            post=posts[post_idx],
            author=users[user_idx]
        )
        db.session.add(comment)
        comments.append(comment)
    
    db.session.commit()
    print(f"✅ Added {len(comments)} engaging comments")
    
    # ============= SHARES =============
    print("\n🔄 Creating share interactions...")
    
    # Popular posts get more shares (post_idx, user_idx)
    shares_data = [
        # Post 2 (Basketball) - Very popular
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
        
        # Post 1 (Welcome) - Popular
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        
        # Post 6 (Beach Cleanup)
        (5, 1), (5, 2), (5, 4), (5, 7),
        
        # Post 4 (Drama)
        (3, 1), (3, 2), (3, 6),
        
        # Post 5 (Computer Lab)
        (4, 2), (4, 3), (4, 5),
        
        # Post 11 (Debate)
        (10, 1), (10, 2), (10, 5),
        
        # Post 9 (Music Concert)
        (8, 1), (8, 6),
        
        # Post 10 (Lunch)
        (9, 4), (9, 7),
    ]
    
    shares = []
    for post_idx, user_idx in shares_data:
        share = Share(
            post=posts[post_idx],
            user=users[user_idx]
        )
        db.session.add(share)
        shares.append(share)
    
    db.session.commit()
    print(f"✅ Added {len(shares)} share interactions")
    
    # ============= SUCCESS SUMMARY =============
    print("\n" + "="*60)
    print("🎉 SUCCESS! Database created and populated!")
    print("="*60)
    print("\n📊 Database Summary:")
    print(f"  • {len(users)} users (2 admins, 7 students)")
    print(f"  • {len(posts)} diverse posts across 8 categories")
    print(f"  • {len(comments)} engaging comments")
    print(f"  • {len(shares)} share interactions")
    print("\n🔐 Login Credentials:")
    print("  Admin:    admin / admin123")
    print("  Editor:   editor_news / editor123")
    print("  Student:  sarah_johnson / student123")
    print("\n💾 Database Location: instance/student_news.db")
    print("✨ Your database is ready and looks professional!")
    print("="*60 + "\n")

if __name__ == "__main__":
    create_database()
