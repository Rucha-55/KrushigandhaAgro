# KrushigandhaAgro

Welcome to **KrushigandhaAgro** – your trusted source for high-quality cattle feed and agricultural products. This repository contains the source code for the KrushigandhaAgro website, which provides information about our products, company details, career opportunities, and an online ordering system.

## 📌 Project Overview
KrushigandhaAgro is dedicated to supporting farmers by providing premium cattle feed and agricultural products. Our platform enables users to explore products, place orders, learn about the company, and apply for career opportunities.

## 🚀 Features
- **Cattle Feed Products**: Browse and order a variety of high-quality cattle feed.
- **Online Ordering**: Easily place orders for cattle feed through the website.
- **Company Information**: Learn about KrushigandhaAgro’s history, mission, and values.
- **Contact Details**: Get in touch with us for inquiries or support.
- **Career Opportunities**: Explore job openings and apply directly through the website.

## 🛠️ Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Django)
- **Database**: SQLite
- **Static Content**: Bootstrap for responsive design

## 📂 Folder Structure
```
KrushigandhaAgro/
├── carrier/        # Career opportunity functionalities
├── contact/        # Contact page logic
├── krushigandha/   # Core application logic
├── media/          # Media files (images, documents)
├── order/          # Order processing system
├── products/       # Product management (cattle feed details)
├── resumes/        # Resume submissions for careers
├── static/         # CSS, JavaScript, and images
├── templates/      # HTML templates for the website
├── db.sqlite3      # SQLite database
└── manage.py       # Django management script
```

## 💻 Installation & Setup
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Rucha-55/KrushigandhaAgro.git
   ```
2. **Navigate to the project folder**:
   ```sh
   cd KrushigandhaAgro
   ```
3. **Create a virtual environment**:
   ```sh
   python3 -m venv env
   ```
4. **Activate the virtual environment**:
   - On Windows:
     ```sh
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source env/bin/activate
     ```
5. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
6. **Apply database migrations**:
   ```sh
   python manage.py migrate
   ```
7. **Run the application**:
   ```sh
   python manage.py runserver
   ```

   The application will be accessible at `http://127.0.0.1:8000/`.



