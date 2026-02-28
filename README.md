# 🚀 SecureBugTracker

SecureBugTracker is a role-based web application built using Flask and SQLite for tracking software bugs securely and efficiently.

It includes authentication, password hashing, and a modern Bootstrap-based UI.

---

## 📌 Features

- 🔐 User Registration & Login
- 🛡 Password Hashing using Werkzeug
- 👥 Role-based Users (Admin, Developer, Tester)
- 🐞 Create and View Bugs
- 📊 Severity-based Visual Indicators
- 🎨 Professional Bootstrap UI
- 🗄 SQLite Database Integration

---

## 🏗 Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite
- Bootstrap 5

---

## 📂 Project Structure
SecureBugTracker/
│
├── app.py
├── models.py
├── templates/
├── static/
├── database.db
├── requirements.txt
└── README.md
---

## 🔧 Installation & Setup

1. Clone the repository:
  git clone https://github.com/YOURUSERNAME/SecureBugTracker.git
  cd SecureBugTracker

2. Create virtual environment:
  python -m venv venv
  venv\Scripts\activate

3. Install dependencies:
  pip install -r requirements.txt

4. Run the application:
  python app.py

5. Open browser:
  http://127.0.0.1:5000


---

## 🔐 Security Features

- Passwords are securely hashed
- Login session management using Flask-Login
- Role-based access control structure
- Input handled through secure Flask forms

---

## 📈 Future Enhancements

- Bug status update functionality
- Role-based permissions (Admin-only actions)
- Search and filter options
- Dashboard analytics
- Deployment to cloud platform

---

## 📄 License

This project is developed for educational and demonstration purposes.

---