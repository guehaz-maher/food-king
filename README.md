# Food King — Professional Full-Stack Restaurant Platform

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14+-red?style=for-the-badge&logo=django)
![React](https://img.shields.io/badge/React-18.0+-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![JWT](https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge&logo=JSON%20web%20tokens)

A high-performance, modular full-stack web application for digital restaurant ordering and management. Built using **Django REST Framework** for the robust backend API architecture and **React** for a responsive, interactive client side.

---

## 🌟 Key Features

* 🔐 **Authentication & Authorization**: Custom JWT-based user roles (Customer, Admin, Delivery Staff).
* 📋 **Dynamic Menu Management**: Structured category listing, auto-slugified URL resources, and full image support via Pillow.
* 🛒 **Order Orchestration**: Real-time order state tracking (`Pending` → `Preparing` → `Ready` → `Delivered`).
* 📦 **Modular System Architecture**: Clean decoupled components (`accounts`, `menu`, `orders`) designed for high maintainability and scalability.

---

## 📐 System Architecture & Data Schema

The platform relies on a normalized relational database design tailored for e-commerce and food delivery services:
+------------------+         +--------------------+         +-------------------+
|  accounts.User   | <------> |    orders.Order    | <-----> |  orders.OrderItem |
+------------------+         +--------------------+         +-------------------+
| - role           |         | - status           |         | - menu_item       |
| - phone_number   |         | - total_price      |         | - quantity        |
| - address        |         | - created_at       |         | - price           |
+------------------+         +--------------------+         +-------------------+
|
v
+-------------------+
|   menu.MenuItem   |
+-------------------+
| - category (FK)   |
| - price           |
| - is_available    |
+-------------------+

---

## 🚀 Tech Stack

### **Backend**
* **Framework:** Django & Django REST Framework (DRF)
* **Authentication:** SimpleJWT (JSON Web Tokens)
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Media Processing:** Pillow (Image Handling)

### **Frontend**
* **Framework:** React.js
* **State Management & Data Fetching:** Axios / Context API
* **Styling:** CSS3 / Modern Flexbox & Grid

---

## 🛠️ Installation & Setup

### Prerequisites
* Python 3.10+
* Node.js & npm

### 1. Backend Setup

```bash
# Clone the repository
git clone [https://github.com/your-username/resto-app.git](https://github.com/your-username/resto-app.git)
cd resto-app

# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install django djangorestframework djangorestframework-simplejwt pillow django-cors-headers

# Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

# Create Superuser (Admin)
python manage.py createsuperuser

# Start Development Server
python manage.py runserver
```
## 2. Frontend setup:
```bash
cd frontend

# Install Dependencies
npm install

# Run Development Server
npm start
```
## Author:
- Maher Guehaz | Full-stack developer
- Github | @maher-guehaz

