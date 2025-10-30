
# Django Portfolio Template

A modern Django-based portfolio template with project showcase, contact form, and visitor logging (IP, ISP, system, browser, timestamp). Each user can add their own profile, skills, and projects using the admin panel.

## Features
- Add/view projects (admin panel)
- Stylish frontend with animations
- Contact form
- Logs visitor info (admin panel)

## Quick Start

1. **Clone the repo:**
   ```sh
   git clone https://github.com/DebaA17/django-project.git
   cd django-project
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv myenv
   source myenv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a superuser (optional, for admin):**
   ```sh
   python manage.py createsuperuser
   ```
6. **Start the server:**
   ```sh
   python manage.py runserver
   ```
7. **Visit:**
   - Home: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Notes
- Do not commit your `db.sqlite3` or `myenv/` folder.
- For production, set `DEBUG = False` and update `ALLOWED_HOSTS` in `settings.py`.

---

**New features coming soon!**

**Note:** This is a portfolio template. When you first run the server, the site will show no projects or profile info. Each user must add their own data (projects, bio, skills, education, achievements, and social links) using the Django admin panel at `/admin`.

This is a simple Django project for 3rd semester students of BPPIMT Salt Lake Campus.
