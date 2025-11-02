import sqlite3
import os

db_path = 'instance/student_news.db'

if not os.path.exists(db_path):
    print("Database not found. Run app.py first to create it.")
    exit(1)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if image_filename column exists
    cursor.execute("PRAGMA table_info(post)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'image_filename' not in columns:
        # Add the image_filename column
        cursor.execute("ALTER TABLE post ADD COLUMN image_filename VARCHAR(255)")
        conn.commit()
        print("✅ Successfully added image_filename column to post table!")
    else:
        print("✅ image_filename column already exists!")
    
    conn.close()
    print("\n🎉 Database migration complete!")
    print("🚀 Now restart the server: python app.py")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Please make sure the database file is not locked by another process.")
