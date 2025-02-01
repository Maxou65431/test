from flask import Flask
from flask import request, jsonify
import requests
import zipfile
import io

# Importe l'application Flask depuis ton fichier flask.py
from flask import app

# L'application que Gunicorn doit exécuter
gunicorn_app = app
