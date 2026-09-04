# 🔐 Secure Login System

### *Flask-Based Authentication System with Advanced Security Features*

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render&logoColor=white)](https://render.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-success)](https://github.com/pradheepa73/-secure-login-system)

### 🌐 [Live Demo](https://secure-login-system-tg6m.onrender.com) | 📂 [GitHub Repository](https://github.com/pradheepa73/-secure-login-system)

---

</div>

## 📖 **Overview**

**Secure Login System** is a professional authentication system built using **Flask**, **SQLite**, and **Bcrypt**. It provides a robust and secure user authentication mechanism with multiple security features to protect user accounts from unauthorized access.

> 🔒 **What makes this system secure?**  
> Password hashing using Bcrypt, account lockout after failed attempts, session management, and duplicate email prevention — all combined to create a secure authentication experience.

---

## ✨ **Features**

| Feature | Description |
|---------|-------------|
| 🔐 **User Registration** | Create new accounts with unique email and password |
| 🔑 **User Login** | Secure login with session management |
| 🛡️ **Password Hashing** | Bcrypt encryption for secure password storage |
| 📋 **Session Management** | Persistent login sessions |
| 📊 **Dashboard Page** | Welcome page after successful login |
| 🚪 **Logout Functionality** | Secure session termination |
| 💬 **Flash Messages** | User-friendly notifications |
| 🚫 **Duplicate Email Detection** | Prevent multiple accounts with same email |
| 📈 **Password Strength Checker** | Real-time password complexity validation |
| 👁️ **Show / Hide Password** | Toggle password visibility |
| 🔢 **Failed Login Attempt Counter** | Track unsuccessful login attempts |
| 🔒 **Account Lock after 3 Failed Attempts** | Temporary account lockout for security |

---

## 🛠️ **Technologies Used**

| Category | Technology |
|----------|------------|
| **Backend** | Python, Flask |
| **Database** | SQLite, SQLAlchemy |
| **Security** | Flask-Bcrypt |
| **Frontend** | HTML, CSS, JavaScript |
| **Deployment** | Render |

---

## 📁 **Project Structure**

```
secure-login-system/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── instance/                  # SQLite database
│
├── static/
│   ├── css/
│   │   └── style.css          # Custom styling
│   └── js/
│       └── script.js          # JavaScript functions
│
└── templates/
    ├── login.html             # Login page
    ├── register.html          # Registration page
    └── dashboard.html         # Dashboard page
```

---

## 📦 **Installation**

### Prerequisites
- Python 3.8 or higher
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/pradheepa73/-secure-login-system.git
cd secure-login-system
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open Browser
```
http://127.0.0.1:5000
```

---

## 🚀 **Live Demo**

🌐 **https://secure-login-system-tg6m.onrender.com**

---

## 🛡️ **Security Features**

| Security Feature | Description |
|------------------|-------------|
| **Bcrypt Password Hashing** | Passwords are securely hashed before storage |
| **Account Lockout** | Users are locked after 3 failed login attempts |
| **Duplicate Email Prevention** | Ensures unique email addresses per account |
| **Session Management** | Secure session handling for login management |
| **Password Strength Checker** | Real-time validation of password complexity |
| **CSRF Protection** | Cross-Site Request Forgery protection |
| **Flash Messages** | Secure notification system for user actions |

---

## 🎯 **Future Improvements**

| Feature | Description |
|---------|-------------|
| 🔄 **Forgot Password** | Password reset via email |
| ✉️ **Email Verification** | Verify user email addresses |
| 🔐 **Two-Factor Authentication (2FA)** | Extra layer of security |
| 👑 **Admin Dashboard** | Manage users and analytics |
| 📧 **Password Reset via Email** | Secure password recovery |

---

## 👤 **Author**

<div align="center">

**Pradheepa M**  
*Cyber Security Enthusiast*

[![GitHub](https://img.shields.io/badge/GitHub-pradheepa73-181717?logo=github)](https://github.com/pradheepa73)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pradheepa-0A66C2?logo=linkedin)](https://linkedin.com/in/pradheepa)

</div>

---

## 📝 **License**

This project is for **educational purposes** and is licensed under the **MIT License**.

---

<div align="center">

### 🔐 *Secure Your Accounts, Stay Safe!*

### Made with ❤️ by Pradheepa M

