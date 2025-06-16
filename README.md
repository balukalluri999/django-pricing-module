Configurable Pricing Module
===========================

Objective:
----------
Design and build a Django web application with a configurable pricing module
that supports differential pricing based on distance, time, and day of the week.

Features:
---------
- Admin panel to configure pricing settings
- Calculate dynamic ride costs
- PostgreSQL integration using Django ORM
- Modular and scalable design

Technologies Used:
------------------
- Python 3.11
- Django 4.x
- PostgreSQL
- Django REST Framework (optional for API exposure)

Project Structure:
------------------
pricing_module/
├── manage.py
├── pricing/                  ← App that handles pricing logic
│   ├── models.py             ← Models with PostgreSQL ArrayField
│   ├── views.py              ← View logic for price calculation
│   ├── serializers.py        ← For API use (optional)
│   ├── admin.py              ← Admin configuration
│   └── ...
├── pricing_module/
│   └── settings.py           ← PostgreSQL DB configured here
└── README.txt                ← This file

Setup Instructions:
-------------------
1. Clone the repo:
   git clone <your-repo-url>

2. Create virtual environment & activate:
   python -m venv env
   source env/bin/activate  (Linux/macOS)
   env\Scripts\activate     (Windows)

3. Install dependencies:
   pip install -r requirements.txt

4. Setup PostgreSQL and update `settings.py`:
   - DB name: pricingdb
   - User: postgres
   - Password: yourpassword

5. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

6. Create superuser:
   python manage.py createsuperuser

7. Start the server:
   python manage.py runserver

8. Access Django Admin:
   http://127.0.0.1:8000/admin/

Author:
-------
Balarajaiah Kalluri
