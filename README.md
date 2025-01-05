# CRM App with Django, Python, and MySQL

A simple Customer Relationship Management (CRM) application built using Django, Python, and MySQL. This app allows users to register, log in, log out, add records, view records, update records, and delete records.

## Features

- **User Authentication**:
  - Register
  - Log In
  - Log Out
- **CRUD Operations**:
  - Add Records
  - View Records
  - Update Records
  - Delete Records

## Requirements

- Python 3.8+
- Django 4.0+
- MySQL Server

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/crm-django-app.git
cd crm-django-app
```

### 2. Create and Activate a Virtual Environment

#### On Windows:
```bash
python -m venv env
env\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database

1. Install MySQL Server and create a database:
   ```sql
   CREATE DATABASE crm_db;
   ```
2. Update the `DATABASES` setting in the `settings.py` file:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'crm_db',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the app.

## Usage

1. **Register:** Create an account.
2. **Log In:** Access your account using your credentials.
3. **Manage Records:** Add, view, update, or delete customer records.
4. **Log Out:** Securely log out of the application.

## Project Structure
```
crm-django-app/
├── crm_app/               # Main app folder
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   ├── views.py          # View logic
│   ├── models.py         # Database models
│   └── urls.py           # URL routing
├── crm_django_app/       # Project settings folder
│   ├── settings.py       # Project settings
│   ├── urls.py           # Project URLs
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Dependencies

- Django
- mysqlclient

Install them with:
```bash
pip install django mysqlclient
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

For questions or support, contact [your email or GitHub profile link].
