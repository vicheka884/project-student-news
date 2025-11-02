@echo off
echo ========================================
echo Student News Blog Website
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting the application...
echo.
echo The website will be available at: http://127.0.0.1:5000
echo.
echo Default Admin Login:
echo Username: admin
echo Password: admin123
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
