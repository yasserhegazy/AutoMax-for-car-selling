# AutoMax 🚗

A modern Django web application for buying and selling cars — built as a full-stack portfolio project.

## Features

- **User Authentication** — Register, login, logout with session management
- **Car Listings** — Create, edit, delete, and browse car listings with images
- **Advanced Filtering** — Filter by brand, transmission, mileage, price, year
- **Sorting** — Sort listings by price, date, or mileage
- **Like System** — Like/unlike listings with AJAX (no page reload)
- **Email Inquiry** — Contact sellers directly via email
- **User Profiles** — Profile photo, bio, location, phone number
- **Responsive Design** — Mobile-first UI with Bootstrap 5
- **Pagination** — Paginated listings with filter preservation

## Tech Stack

| Category | Technology |
|----------|-----------|
| Backend | Django 6, Python 3.12 |
| Frontend | Bootstrap 5, jQuery, Bootstrap Icons |
| Database | SQLite (dev), PostgreSQL-ready |
| Forms | django-crispy-forms + Bootstrap 5 |
| Filtering | django-filter |
| Deployment | Gunicorn, WhiteNoise |

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yasserhegazy/AutoMax-for-car-selling
cd AutoMax-for-car-selling

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EOF

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the landing page.

## Project Structure

```
AutoMax/
├── automax/          # Project settings & config
├── main/             # Car listings app (models, views, templates)
│   ├── models.py     # Listing, LikedListing models
│   ├── views.py      # All listing views (CRUD, like, inquire)
│   ├── filters.py    # django-filter configuration
│   ├── templates/    # HTML templates
│   └── static/       # CSS, JS, images, videos
├── users/            # User management app
│   ├── models.py     # Profile, Location models
│   ├── views.py      # Auth & profile views
│   └── templates/    # Auth & profile templates
├── media/            # User-uploaded files
├── manage.py
├── requirements.txt
└── Procfile          # Production deployment
```

## Deployment

The project is production-ready with:
- **WhiteNoise** for static file serving
- **Gunicorn** as WSGI server
- **Environment variables** via django-environ
- **Procfile** for Heroku/Railway/Render

Set these environment variables in production:
```
SECRET_KEY=<strong-random-key>
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
EMAIL_HOST_USER=<your-email>
EMAIL_HOST_PASSWORD=<your-password>
```
