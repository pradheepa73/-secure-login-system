# Secure Login System

A secure login and registration system built using Flask, SQLite, SQLAlchemy, and Bcrypt.

## Features

- User Registration
- User Login
- Password Hashing using Bcrypt
- Session Management
- Dashboard Page
- Logout Functionality
- Flash Messages
- Duplicate Email Detection
- Password Strength Checker
- Show / Hide Password
- Failed Login Attempt Counter
- Account Lock after 3 Failed Attempts

## Technologies Used

- Python
- Flask
- SQLite
- SQLAlchemy
- Flask-Bcrypt
- HTML
- CSS
- JavaScript

## Project Structure

```text
secure-login-system/
│
├── app.py
├── requirements.txt
├── README.md
├── instance/
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html

    Installation
Clone the repository

git clone <your-github-repo-link>
Open project folder

cd secure-login-system
Create virtual environment

python -m venv venv
Activate virtual environment

Windows
venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Run the Flask application

python app.py
Open browser

http://127.0.0.1:5000

Security Features

-Passwords are securely hashed using Bcrypt.

-Users are locked after 3 failed login attempts.

-Duplicate email registration is prevented.

-Sessions are used for secure login management.

Future Improvements
-Forgot Password Feature

-Email Verification

-Two-Factor Authentication (2FA)

-Admin Dashboard

-Password Reset via Email

Author
Pradheepa.M

