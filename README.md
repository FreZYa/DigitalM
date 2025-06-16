# Digital Marketing Project

A Django-based digital marketing application.

## Setup

1. Clone the repository
```bash
git clone <repository_url>
cd digitalm
```

2. Create and activate virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
cd mysite
python manage.py migrate
```

5. Run server
```bash
python manage.py runserver
```

## Project Structure

- `mysite/` - Main Django project directory
  - `myapp/` - Django application
  - `uploads/` - User uploaded files

## License

[Add license information] 