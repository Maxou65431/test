from flask import Flask  # Assure-toi que Flask est bien importé
from flask import request, jsonify
import requests
import zipfile
import io
import os

from flask import app as application  # 🔹 Importe ton app Flask depuis ton fichier principal

if __name__ != "__main__":
    gunicorn_app = application  # 🔹 Gunicorn peut maintenant appeler gunicorn_app
