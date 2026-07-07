# 🚀 Nandini Y. — Premium Portfolio Website

A modern, production-ready Full Stack Developer portfolio built with **Django**, **Tailwind CSS**, **Vanilla JavaScript**, and **MySQL**.

---

## ✨ Features

- 🎨 **Premium dark UI** with glassmorphism, gradients, and smooth animations
- 📱 **Fully responsive** (320px → 1920px)
- ⚡ **Typing animation** in the Hero section
- 🌟 **Scroll reveal animations** using IntersectionObserver
- 📊 **Animated skill bars** and counter statistics
- 📬 **AJAX contact form** with MySQL storage and real-time validation
- 🎯 **Active section highlighting** in the sticky navbar
- 🔝 **Back-to-top** floating button
- 🌐 **SEO optimized** with proper meta tags and semantic HTML

---

## 🛠️ Tech Stack

| Layer      | Technology                         |
|------------|------------------------------------|
| Backend    | Python 3.11, Django 4.2            |
| Frontend   | HTML5, Tailwind CSS 3.4, Vanilla JS|
| Database   | MySQL 8.x                          |
| Connector  | pymysql                            |
| Static     | WhiteNoise                         |
| Icons      | Font Awesome 6.5                   |
| Fonts      | Google Fonts (Outfit + Inter)      |

---

## 📁 Project Structure

```
Portfolio/
├── portfolio/          # Django core (settings, urls, wsgi)
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
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/NandiniY018/portfolio.git
cd portfolio
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up MySQL Database
Open MySQL Workbench or your terminal and run:
```sql
CREATE DATABASE portfolio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Configure Database Credentials
Edit `portfolio/settings.py` and update:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'portfolio_db',
        'USER': 'root',           # Your MySQL username
        'PASSWORD': 'your_pass',  # Your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (for Admin)
```bash
python manage.py createsuperuser
```

### 7. Add Resume PDF
Place your resume PDF at `static/resume.pdf`

### 8. Run the Development Server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

Admin panel: **http://127.0.0.1:8000/admin**

---

## 🎨 Customization

### Update Your Info
Edit these template partials in `templates/partials/`:
- **`hero.html`** — Name, title, social links
- **`about.html`** — Bio, personal info, stats
- **`experience.html`** — Job titles, companies, responsibilities
- **`projects.html`** — Project details, links
- **`education.html`** — Institution names, grades
- **`certificates.html`** — Certificate links
- **`contact.html`** — Email, phone, social links
- **`footer.html`** — Copyright, links

### Update Project Images
Replace these files in `static/images/`:
- `profile.png` — Your profile photo (square, min 300×300px)
- `project-ecommerce.png` — E-Commerce project screenshot
- `project-crop.png` — Crop Yield project screenshot
- `project-grocery.png` — Grocery project screenshot

---

## 📬 Contact Form

The contact form uses Django's AJAX endpoint to save messages to MySQL.
View submissions in the Django admin at `/admin/website/contactmessage/`.

---

## 🚀 Production Deployment

For production, set in `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'your-secure-secret-key'
```

Then collect static files:
```bash
python manage.py collectstatic
```

---

## 📄 License

This project is licensed under the MIT License.

---

*Built with ❤️ by Nandini Y.*
