from app import app  # Si ton fichier s'appelle maintenant app.py

if __name__ != "__main__":
    gunicorn_app = app
