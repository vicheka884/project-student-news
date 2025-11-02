import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the student_news database"""
    try:
        # Connect to MySQL server (without database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS student_news")
            print("✅ Database 'student_news' created successfully!")
            
            cursor.close()
            connection.close()
            
    except Error as e:
        print(f"❌ Error: {e}")

def create_tables():
    """Create all tables for Student News"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='student_news',
            user='root',
            password='root'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(80) UNIQUE NOT NULL,
                    email VARCHAR(120) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    is_admin BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("✅ Users table created!")
            
            # Posts table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS posts (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(200) NOT NULL,
                    content TEXT NOT NULL,
                    category VARCHAR(50) NOT NULL,
                    image_filename VARCHAR(255),
                    author_id INT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
                )
            """)
            print("✅ Posts table created!")
            
            # Comments table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS comments (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    content TEXT NOT NULL,
                    post_id INT NOT NULL,
                    author_id INT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
                    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
                )
            """)
            print("✅ Comments table created!")
            
            # Shares table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS shares (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    post_id INT NOT NULL,
                    user_id INT NOT NULL,
                    shared_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                )
            """)
            print("✅ Shares table created!")
            
            connection.commit()
            cursor.close()
            connection.close()
            print("\n🎉 All tables created successfully!")
            
    except Error as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n🗄️  Creating MySQL Database for Student News\n")
    create_database()
    print()
    create_tables()