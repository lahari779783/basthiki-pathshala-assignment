# 🏫 Basti Ki Pathshala - Volunteer Management System

A simple Flask-based web application to register, view, edit, and delete volunteers for **Basti Ki Pathshala**.

## 🚀 Features

- Volunteer registration form
- Admin dashboard to view all volunteers
- Edit and delete volunteer information
- Responsive UI with Bootstrap
- SQLite database integration

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap, Jinja2
- **Backend:** Python, Flask
- **Database:** SQLite

## 📂 Project Structure

basthiki_pathshala_assignment/
│
├── backend/
│ ├── static/
│ │ └── images/
│ ├── templates/
│ │ ├── index.html
│ │ ├── register.html
│ │ ├── admin.html
│ │ └── edit.html
│ ├── volunteers.db
│ └── app.py
│
└── README.md

bash
Copy code

## ▶️ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/lahari779783/basthiki-pathshala-assignment.git
   cd basthiki-pathshala-assignment/backend
(Optional) Create virtual environment:



python -m venv .venv
.venv\Scripts\activate  # For Windows
Install dependencies:



pip install flask
Run the application:


python app.py
Open your browser and visit:

http://127.0.0.1:5000/
