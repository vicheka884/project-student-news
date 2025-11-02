# 🚀 MySQL Setup Guide for Student News Hub

## Step 1: Start MySQL Service

### Option A: XAMPP (Recommended)
1. Open XAMPP Control Panel
2. Start the **MySQL** service (click "Start")
3. Wait for it to turn green

### Option B: Command Line
```bash
# Start MySQL service (Admin privileges may be required)
net start mysql
```

## Step 2: Configure Database Credentials

Update `create_mysql_db.py` with your MySQL password:

```python
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_PASSWORD_HERE'  # ← Replace with your actual password
}
```

Common passwords to try:
- `''` (empty password)
- `'root'`
- `'password'`
- `'123456'`

## Step 3: Update App Configuration

Update `app.py` line 20 with the same password:

```python
# Replace YOUR_PASSWORD with your actual MySQL password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:YOUR_PASSWORD@localhost/student_news'
```

## Step 4: Test MySQL Connection

Run this to test your credentials:

```bash
python create_mysql_db.py
```

## Step 5: If Connection Works

✅ **Success!** Your MySQL database is now connected and populated with professional data!

## 🔧 Troubleshooting

### Error: "Can't connect to MySQL server"
- Make sure MySQL service is **STARTED** in XAMPP
- Check if port 3306 is open (default MySQL port)

### Error: "Access denied for user 'root'@'localhost'"
- Wrong password: Update both files with correct password
- Try empty password: `'password': ''`

### Error: "Module 'pymysql' not found"
```bash
pip install PyMySQL
```

## 📊 Professional Database Contents

After setup, you'll have:

- **9 diverse users** (admins, editors, students)
- **15 engaging posts** (sports, arts, tech, community, etc.)
- **27 realistic comments** with emojis
- **29 share interactions**

## 🔐 Login Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |
| Editor | `editor_news` | `editor123` |
| Student | `sarah_johnson` | `student123` |

## 🔄 Switching Back to SQLite

If you want to use SQLite instead:

1. Open `app.py`
2. Comment line 20 and uncomment line 24:

```python
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/student_news'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_news.db'
```

3. Run: `python create_db.py` (for SQLite)

---

**Need Help?** Check that:
- ✅ MySQL is installed and running
- ✅ Password is correct in both files
- ✅ Database name is `student_news`
- ✅ PyMySQL package is installed (`pip install PyMySQL`)

**Ready to connect?** Follow the steps above and run `python create_mysql_db.py`! 🎉
