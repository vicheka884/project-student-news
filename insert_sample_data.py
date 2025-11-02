import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

def insert_sample_data():
    """Insert rich sample data for a professional-looking database"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='student_news',
            user='root',
            password='root'
        )
        
        cursor = connection.cursor()
        
        # ============= USERS =============
        print("👥 Creating diverse users...")
        
        users = [
            ('admin', 'admin@studentnews.com', 'admin123', True),
            ('sarah_johnson', 'sarah.j@student.edu', 'student123', False),
            ('michael_chen', 'michael.c@student.edu', 'student123', False),
            ('emily_rodriguez', 'emily.r@student.edu', 'student123', False),
            ('david_kim', 'david.k@student.edu', 'student123', False),
            ('sophia_patel', 'sophia.p@student.edu', 'student123', False),
            ('james_williams', 'james.w@student.edu', 'student123', False),
            ('olivia_brown', 'olivia.b@student.edu', 'student123', False),
            ('editor_news', 'editor@studentnews.com', 'editor123', True),
        ]
        
        for username, email, password, is_admin in users:
            password_hash = generate_password_hash(password)
            cursor.execute("""
                INSERT INTO users (username, email, password_hash, is_admin)
                VALUES (%s, %s, %s, %s)
            """, (username, email, password_hash, is_admin))
        
        print("✅ Created 9 diverse users (2 admins, 7 students)")
        
        # ============= POSTS =============
        print("\n📰 Creating engaging posts...")
        
        posts = [
            {
                'title': '🎓 Welcome to Student News Hub!',
                'content': 'Welcome to our brand new Student News platform! This is your one-stop destination for all campus news, events, and updates. Stay connected with your fellow students, share your achievements, and never miss an important announcement. We\'re excited to have you here!',
                'category': 'Announcements',
                'author_id': 1
            },
            {
                'title': '🏀 Basketball Team Clinches State Championship',
                'content': 'In a thrilling overtime victory, our varsity basketball team secured the state championship title last night! The final score was 78-75 against North Valley High. Senior captain Marcus Thompson scored a career-high 32 points. The team showed incredible determination and teamwork throughout the season. Congratulations to Coach Rodriguez and the entire team! 🏆',
                'category': 'Sports',
                'author_id': 2
            },
            {
                'title': '🔬 Annual Science Fair - Next Wednesday',
                'content': 'Mark your calendars! Our Annual Science Fair is happening next Wednesday, November 6th, in the main gymnasium from 9 AM to 4 PM. Over 150 students will be showcasing their innovative projects ranging from robotics to environmental science. Special guest judges include Dr. Amanda Lewis from MIT and Professor Chen from Stanford University. All students, parents, and faculty are welcome to attend!',
                'category': 'Events',
                'author_id': 9
            },
            {
                'title': '🎭 Drama Club Presents "Romeo & Juliet"',
                'content': 'The Drama Club is proud to announce our fall production of Shakespeare\'s timeless classic "Romeo & Juliet". Performances will be held November 15-17 at 7 PM in the school auditorium. Tickets are $10 for students and $15 for adults, available at the door or through our online portal. Don\'t miss this spectacular performance featuring our talented student actors!',
                'category': 'Arts',
                'author_id': 3
            },
            {
                'title': '💻 New Computer Lab Opens in West Wing',
                'content': 'Great news for tech enthusiasts! The school has opened a state-of-the-art computer lab in the West Wing. The facility features 40 new workstations with the latest software for coding, graphic design, and video editing. The lab is available to all students during school hours and until 6 PM on weekdays. Special thanks to our IT department and generous donors who made this possible!',
                'category': 'Technology',
                'author_id': 4
            },
            {
                'title': '🌍 Environmental Club Beach Cleanup Success',
                'content': 'Last Saturday, 75 students from our Environmental Club participated in a beach cleanup at Ocean View Beach. Together, we collected over 300 pounds of trash and recyclables! The event was a huge success and we\'re already planning our next cleanup for December. Thank you to everyone who participated and helped make our beaches cleaner! 🌊♻️',
                'category': 'Community',
                'author_id': 5
            },
            {
                'title': '📚 Library Extended Hours During Finals',
                'content': 'Attention all students: The library will be extending its hours during finals week (December 11-15). We\'ll be open from 7 AM to 10 PM to provide you with a quiet study space. Free coffee and snacks will be available in the study lounge. Librarians will also be available for research assistance. Good luck with your exams!',
                'category': 'Announcements',
                'author_id': 9
            },
            {
                'title': '⚽ Soccer Team Seeks New Players',
                'content': 'Our girls\' soccer team is looking for new players for the spring season! No experience necessary - just bring your enthusiasm and willingness to learn. Tryouts will be held on November 8th and 9th from 3:30-5:00 PM on the main field. All grades welcome. Contact Coach Martinez at athletics@school.edu for more information.',
                'category': 'Sports',
                'author_id': 6
            },
            {
                'title': '🎵 Music Department Concert This Friday',
                'content': 'Join us this Friday evening for our Fall Concert featuring the school band, orchestra, and choir! The concert starts at 7 PM in the auditorium. Our talented musicians have been practicing all semester and are excited to share their performances with you. Admission is free, and light refreshments will be served. Bring your family and friends!',
                'category': 'Arts',
                'author_id': 7
            },
            {
                'title': '🍕 New Lunch Menu Options Available',
                'content': 'The cafeteria has introduced exciting new lunch options based on student feedback! Now featuring vegetarian and vegan meals, a fresh salad bar, and international cuisine rotating weekly. This week\'s special: Authentic Mexican street tacos on Tuesday and Thai curry on Thursday. Don\'t forget to fill out the survey to suggest more menu items!',
                'category': 'Campus Life',
                'author_id': 8
            },
            {
                'title': '🏆 Debate Team Takes Regional Championship',
                'content': 'Congratulations to our debate team for winning the Regional Debate Championship! Seniors Alex Thompson and Maria Garcia took first place in the policy debate category, while junior Ethan Park secured second place in Lincoln-Douglas debate. The team will advance to the state competition in January. Way to represent our school! 🎤',
                'category': 'Academics',
                'author_id': 9
            },
            {
                'title': '🚗 New Student Parking Rules',
                'content': 'Important update for all students with parking permits: Starting November 1st, new parking regulations will be in effect. Please park only in designated student areas (Lots B and C). Faculty parking (Lot A) is strictly off-limits. Violators will receive warnings and potential permit revocation. Digital permits must be displayed on your dashboard. Visit the office for more details.',
                'category': 'Announcements',
                'author_id': 1
            },
            {
                'title': '🎨 Student Art Exhibition Opens Next Month',
                'content': 'The Visual Arts department is thrilled to announce our annual Student Art Exhibition opening December 1st! The exhibition will showcase paintings, sculptures, photography, and digital art created by our talented students throughout the semester. Opening reception on December 1st at 6 PM with refreshments. The exhibition runs through December 15th.',
                'category': 'Arts',
                'author_id': 3
            },
            {
                'title': '🤝 Community Service Day - November 18th',
                'content': 'Save the date for our school-wide Community Service Day on November 18th! Students will participate in various service projects including park beautification, senior center visits, food bank volunteering, and tutoring at elementary schools. This is a great opportunity to give back to our community and earn service hours. Sign-up sheets available in the main office!',
                'category': 'Community',
                'author_id': 5
            },
            {
                'title': '📱 New School Mobile App Launched',
                'content': 'Stay connected on the go with our new school mobile app! Available now on iOS and Android. Features include: real-time announcements, class schedules, grades, cafeteria menu, event calendar, and emergency notifications. Download it today from the App Store or Google Play by searching "Student News Hub". Your login credentials are the same as your student portal.',
                'category': 'Technology',
                'author_id': 4
            },
        ]
        
        for post in posts:
            cursor.execute("""
                INSERT INTO posts (title, content, category, author_id)
                VALUES (%s, %s, %s, %s)
            """, (post['title'], post['content'], post['category'], post['author_id']))
        
        print(f"✅ Created {len(posts)} engaging posts across multiple categories")
        
        # ============= COMMENTS =============
        print("\n💬 Adding realistic comments...")
        
        comments = [
            # Comments on post 1 (Welcome)
            (1, 2, "Love the new platform! So much easier to stay updated now. 😊"),
            (1, 3, "This is awesome! Great work on the design."),
            (1, 5, "Finally! Been waiting for something like this."),
            
            # Comments on post 2 (Basketball)
            (2, 4, "What an amazing game! So proud of our team! 🏀🔥"),
            (2, 6, "Marcus Thompson is a legend! That final shot was incredible!"),
            (2, 7, "Best game I've ever watched! Congratulations team!"),
            (2, 3, "Coach Rodriguez deserves a lot of credit. Great season!"),
            
            # Comments on post 3 (Science Fair)
            (3, 5, "Can't wait to see all the projects! I'm presenting my robotics project."),
            (3, 4, "Will there be livestream for parents who can't attend?"),
            (3, 8, "I heard there are some really impressive AI projects this year!"),
            
            # Comments on post 4 (Drama)
            (4, 7, "Already got my tickets! The cast is incredible this year."),
            (4, 2, "I'm playing Mercutio! Hope to see everyone there! 🎭"),
            
            # Comments on post 5 (Computer Lab)
            (5, 4, "Finally! The old computers were so slow. This is game-changing."),
            (5, 3, "Perfect timing with the coding competition coming up!"),
            (5, 6, "Can we use it for gaming club meetings?"),
            
            # Comments on post 6 (Beach Cleanup)
            (6, 2, "So proud of everyone who showed up! Great turnout."),
            (6, 8, "Count me in for the next one! This was so rewarding."),
            (6, 5, "Thanks to everyone who helped organize this! 🌊"),
            
            # Comments on post 7 (Library Hours)
            (7, 3, "This is exactly what we needed! Thank you!"),
            (7, 6, "Free coffee during finals? You're the best! ☕"),
            
            # Comments on post 9 (Music Concert)
            (9, 7, "I'll be playing violin in the orchestra! Hope you can make it!"),
            (9, 2, "The choir sounds amazing this year. Don't miss it!"),
            
            # Comments on post 10 (Lunch Menu)
            (10, 8, "Finally some vegan options! Thank you so much! 🌱"),
            (10, 5, "Those tacos were delicious! Best cafeteria food ever!"),
            (10, 4, "Can we get sushi next? That would be amazing!"),
            
            # Comments on post 11 (Debate Team)
            (11, 3, "Congratulations! You all worked so hard for this."),
            (11, 6, "Alex and Maria are unstoppable! Good luck at state!"),
        ]
        
        for post_id, author_id, content in comments:
            cursor.execute("""
                INSERT INTO comments (content, post_id, author_id)
                VALUES (%s, %s, %s)
            """, (content, post_id, author_id))
        
        print(f"✅ Added {len(comments)} engaging comments")
        
        # ============= SHARES =============
        print("\n🔄 Creating share interactions...")
        
        # Popular posts get more shares
        shares = [
            # Post 2 (Basketball) - Very popular
            (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
            
            # Post 1 (Welcome) - Popular
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
            
            # Post 6 (Beach Cleanup)
            (6, 2), (6, 3), (6, 5), (6, 8),
            
            # Post 4 (Drama)
            (4, 2), (4, 3), (4, 7),
            
            # Post 5 (Computer Lab)
            (5, 3), (5, 4), (5, 6),
            
            # Post 11 (Debate)
            (11, 2), (11, 3), (11, 6),
            
            # Post 9 (Music Concert)
            (9, 2), (9, 7),
            
            # Post 10 (Lunch)
            (10, 5), (10, 8),
        ]
        
        for post_id, user_id in shares:
            cursor.execute("""
                INSERT INTO shares (post_id, user_id)
                VALUES (%s, %s)
            """, (post_id, user_id))
        
        print(f"✅ Added {len(shares)} share interactions")
        
        # Commit all changes
        connection.commit()
        cursor.close()
        connection.close()
        
        print("\n" + "="*60)
        print("🎉 SUCCESS! Database populated with rich sample data!")
        print("="*60)
        print("\n📊 Database Summary:")
        print(f"  • 9 users (2 admins, 7 students)")
        print(f"  • 15 diverse posts across 8 categories")
        print(f"  • {len(comments)} engaging comments")
        print(f"  • {len(shares)} share interactions")
        print("\n🔐 Login Credentials:")
        print("  Admin: admin / admin123")
        print("  Editor: editor_news / editor123")
        print("  Student: sarah_johnson / student123")
        print("\n✨ Your database is now ready and looks professional!")
        
    except Error as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("📝 CREATING PROFESSIONAL DATABASE")
    print("="*60 + "\n")
    insert_sample_data()