Shift Scheduling System

📌 Overview

This is a web-based shift scheduling system built with Flask. The project provides an intuitive interface to manage and assign shifts efficiently.

🚀 Features

User-friendly interface for scheduling shifts

Role-based access control (admin, staff, etc.)

Automatic shift conflict detection

Database integration for storing schedules

API endpoints for data retrieval

🛠 Technologies Used

Flask (Backend Framework)

SQLite/MySQL/PostgreSQL (Database)

HTML, CSS, JavaScript (Frontend)

Bootstrap/Tailwind (Styling)

Jinja2 (Templating Engine)

🔧 Installation

Clone the repository:

git clone https://github.com/your-username/your-repository.git
cd your-repository

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Set up the database:

flask db init
flask db migrate -m "Initial migration."
flask db upgrade

Run the application:

flask run

The application will be available at http://127.0.0.1:5000/

📂 Project Structure

/your-repository
│-- app/
│   │-- templates/
│   │-- static/
│   │-- routes.py
│   │-- models.py
│-- migrations/
│-- venv/
│-- config.py
│-- requirements.txt
│-- run.py

🤝 Contribution

Contributions are welcome! To contribute:

Fork the repository

Create a new branch (git checkout -b feature-branch)

Commit your changes (git commit -m "Added a new feature")

Push to your fork (git push origin feature-branch)

Open a Pull Request

📜 License

This project is licensed under the MIT License.

📧 Contact

Author: Pedro Martins

Email: pedromgs23@gmail.com

GitHub: PEDR8K





