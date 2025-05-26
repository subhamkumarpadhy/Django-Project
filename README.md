# 🧵 Threads by Subham

**Threads by Subham** is a lightweight, fully functional social media web application built using Django. It allows users to register, log in, create threads (text posts with optional images), and view threads posted by others. The application is designed with simplicity, responsiveness, and functionality in mind.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Secure sign-up and login system
  - Logout functionality
- 📝 **Thread Creation**
  - Add a text-based thread with optional image upload
  - Threads are displayed in reverse chronological order
- 🧾 **User Dashboard**
  - View your threads
  - Edit or delete your own threads
- 🔍 **Search Functionality**
  - Search threads based on keywords
- 📱 **Responsive UI**
  - Clean and mobile-friendly interface using Bootstrap 5

---

## 🖥️ Tech Stack

- **Backend**: Django 5.0.6
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.3
- **Database**: SQLite3 (default Django DB)
- **Python Version**: 3.12 or later

---

## 📂 Project Structure

Django-Project/
│
├── threads/ # Main Django app
│ ├── migrations/
│ ├── static/ # Static files (CSS, JS, images)
│ ├── templates/ # HTML templates
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── Django_Project/ # Project settings and URLs
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── media/ # Uploaded thread images
├── db.sqlite3 # SQLite database
├── requirements.txt # Python dependencies
└── manage.py # Django management script

---

## ⚙️ Installation and Setup

1. **Clone the Repository**
   -- git clone https://github.com/subhamkumarpadhy/Django-Project.git
   -- cd Django-Project
2. **Create and Activate Virtual Environment**
   -- python -m venv venv
   --source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependencies**
   -- pip install -r requirements.txt
4. **Apply Migrations**
   -- python manage.py migrate
5. **Run the Server**
   -- python manage.py runserver
6. **Open in Browser**
   -- http://127.0.0.1:8000/

## 🙋‍♂️ Author
  Subham Kumar Padhy
 🔗 GitHub

## ⭐ If you found this project helpful or interesting, consider giving it a star!
