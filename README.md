# Nandini Y. — Premium Portfolio Website

A modern, production-ready Full Stack Developer portfolio built with **Django**, **Tailwind CSS**, **Vanilla JavaScript**, and **MySQL/PostgreSQL**.

---

## Features

- **Premium dark UI** with glassmorphism, gradients, and smooth animations
- **Fully responsive** (320px → 1920px)
- **Typing animation** in the Hero section
- **Scroll reveal animations** using IntersectionObserver
- **Dynamic Site Settings & Resume Management** configurable directly from the Django Admin
- **AJAX contact form** with database storage and real-time validation
- **SEO optimized** with proper meta tags and semantic HTML

---

## Tech Stack

| Layer      | Technology                                    |
|------------|-----------------------------------------------|
| Backend    | Python 3.11, Django 6.0                       |
| Frontend   | HTML5, Tailwind CSS 3.4, Vanilla JS           |
| Database   | PostgreSQL/MySQL (via `DATABASE_URL`), SQLite3|
| Static     | WhiteNoise                                    |
| Icons      | Font Awesome 6.5                              |
| Fonts      | Google Fonts (Outfit + Inter)                 |

---

## Project Structure

```text
Portfolio/
├── portfolio/          # Django core (settings, urls, wsgi/asgi)
├── website/            # Portfolio app (models, views, urls)
├── templates/          # All HTML templates
│   ├── base.html       # Base layout (Tailwind, Fonts, CSS, JS)
│   ├── home.html       # Single-page home
│   └── partials/       # Section partials (hero, about, skills, ...)
├── static/
│   ├── css/global.css  # Premium design system & animations
│   ├── js/main.js      # All interactive behavior
│   └── images/         # Profile photo & project screenshots
├── media/              # Uploaded files (resume PDF etc.)
├── docker-compose.yml  # Docker environment setup
├── manage.py
├── requirements.txt
└── README.md
```

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/NandiniY018/portfolio.git
cd portfolio
```

### 2. Install Python dependencies
```bash
# Recommended to use a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory alongside `manage.py` and configure the following variables (or let them fallback to defaults):
```env
DEBUG=True
SECRET_KEY=your-secure-secret-key
DATABASE_URL=mysql://root:your_pass@localhost:3306/portfolio_db # Optional (defaults to sqlite3)
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

### 4. Run Migrations & Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Application
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

---

## Admin Panel & Content Management

Visit the Admin panel at **http://127.0.0.1:8000/admin** to:
1. Update your global settings and SEO tags under **Site Settings**.
2. Manage and activate your CV/Resume under **Resumes**.
3. Add or edit your Projects, Skills, Experiences, Education, and Certificates.
4. View all incoming messages submitted through the Contact Form.

---

## Production Deployment

For production, ensure your `.env` contains:
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgres://user:pass@db-host:5432/dbname
```
Then collect static files:
```bash
python manage.py collectstatic
```

You can use Docker Compose to spin up the entire stack in a production-like environment:
```bash
docker-compose up -d --build
```

---

## License

This project is licensed under the MIT License.

---

*Built by Nandini Y.*
