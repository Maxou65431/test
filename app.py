from flask import Flask, request, jsonify
import requests
import zipfile
import io

app = Flask(__name__)  # ✅ L'application doit être définie ici

DATA_TOURISME_URL = "https://diffuseur.datatourisme.fr/webservice/76e20e98d8ed6a9c0c05b7547e51210f/41e828b6-39e1-422a-9b04-2b72c6c3734a"

@app.route("/get-json", methods=["GET"])
def get_json():
    app_key = request.args.get("app_key")  # Récupère la clé API
    if not app_key:
        return jsonify({"error": "Missing app_key"}), 400

    # Télécharger et décompresser le fichier ZIP
    response = requests.get(DATA_TOURISME_URL, stream=True)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch ZIP file"}), 500

    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        extracted_data = {file: z.read(file).decode("utf-8") for file in z.namelist() if file.endswith(".json")}

    return jsonify(extracted_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # ✅ Flask s'exécute ici
