from flask import Flask, request, jsonify
import requests
import zipfile
import io
import os

app = Flask(__name__)

DATA_TOURISME_URL = "https://diffuseur.datatourisme.fr/webservice/76e20e98d8ed6a9c0c05b7547e51210f/41e828b6-39e1-422a-9b04-2b72c6c3734a"

@app.route("/get-json", methods=["GET"])
def get_json():
    app_key = request.args.get("app_key")  # Récupère la clé API de l'URL
    if not app_key:
        return jsonify({"error": "Missing app_key"}), 400

    # Télécharger le fichier ZIP depuis l'API DataTourisme
    url = DATA_TOURISME_URL.replace("{app_key}", app_key)
    response = requests.get(url, stream=True)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch ZIP file"}), 500

    # Décompresser le fichier ZIP
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        extracted_data = {}
        for file in z.namelist():
            if file.endswith(".json"):  # Filtrer uniquement les JSON
                with z.open(file) as json_file:
                    extracted_data[file] = json_file.read().decode("utf-8")

    return jsonify(extracted_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
