# IS218FinalProject
This is the Final Project for IS218 offerred at NJIT. 

## Quick Start (Windows Command Prompt)

1. Create and activate virtual environment:

```bat
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bat
pip install -r requirements.txt
```

3. Run migrations:

```bat
python manage.py makemigrations
python manage.py migrate
```

4. Create admin user:

```bat
python manage.py createsuperuser
```

5. Start development server:

```bat
python manage.py runserver
```

6. Open in browser:

- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Accounts: http://127.0.0.1:8000/accounts/

## Notes

- Project spec details were moved to PROJECT_REQUIREMENTS.md.
- Current starter routes are wired for pages and accounts so you can begin building features immediately.
