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

3. Install dependencies
   

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

## 📡 API Endpoints

This module provides RESTful APIs to manage pricing configurations and calculate ride fares.

---

### 🔧 Pricing Configuration Endpoints

| Method | Endpoint                  | Description                          |
|--------|---------------------------|--------------------------------------|
| GET    | `http://127.0.0.1:8000/api/config/create/`           | List all pricing configurations      |
| POST   | `http://127.0.0.1:8000/api/config/create/`           | Create a new pricing configuration   |
| GET    | `/api/configs/<id>/`      | Retrieve a specific configuration    |
| PUT    | `/api/configs/<id>/`      | Update a pricing configuration       |
| DELETE | `/api/configs/<id>/`      | Delete a pricing configuration       |

---

### 💰 Price Calculation Endpoint

| Method | Endpoint                 | Description                           |
|--------|--------------------------|---------------------------------------|
| POST   | ` http://127.0.0.1:8000/api/calculate-price/`  | Calculate ride price dynamically      |

---

## 🧪 Sample API Payloads

---

### ✅ Create a Pricing Configuration

**POST** `http://127.0.0.1:8000/api/config/create/`

```json
{
    "name": "Standard Mon",
    "is_active": true,
    "base_price": 100,
    "base_distance": 5,
    "additional_price_per_km": 12.5,
    "days_active": [
        "Mon"
    ]
}

### 💰 Price Calculation Endpoint

**POST** `/api/calculate-price/`

This endpoint calculates the total fare of a ride based on:

- Distance traveled (in kilometers)
- Duration (in minutes)
- waiting minutes
- date (in `HH:MM:SS` format)

---

#### ✅ Sample Request Payload

```json
{
  "distance_km": 10,
  "ride_minutes": 25,
  "waiting_minutes": 10,
  "date": "2025-06-16"
}

Author:
-------
Balarajaiah Kalluri
