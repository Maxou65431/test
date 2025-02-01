from flask import Flask  # ✅ Flask doit être importé correctement
from flask import app  # ❌ Mauvais import

# ✅ Solution correcte
from flask import app

gunicorn_app = app  # ✅ Gunicorn peut appeler gunicorn_app
