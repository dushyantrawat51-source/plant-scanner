from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from health import check_health
app = Flask(__name__)
CORS(app)

API_KEY = "2b10LtosAzCdUQ9aBjklIkle"
@app.route("/")
def home():
    return "Plant Scanner Backend Running!"

@app.route("/identify", methods=["POST"])
def identify():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    image = request.files["image"]

    url = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

    files = {
        "images": (
            image.filename,
            image.stream,
            image.mimetype
        )
    }

    response = requests.post(url, files=files)

    plant_data = response.json()

    if len(plant_data.get("results", [])) > 0:

        best_match = plant_data["results"][0]

        plant_name = best_match["species"]["commonNames"][0] if best_match["species"]["commonNames"] else "Unknown"

        scientific_name = best_match["species"]["scientificNameWithoutAuthor"]

    else:

        plant_name = "Unknown"
        scientific_name = "Unknown"

    health_result = check_health("leaf.jpg")

    return jsonify({
        "plant_name": plant_name,
        "scientific_name": scientific_name,
        "health": health_result.get("health", "Unknown"),
        "disease": health_result.get("disease", "Unknown"),
        "confidence": health_result.get("confidence", 0),
        "remedy": health_result.get("suggestion", "No remedy available")
    })
``
    image = request.files["image"]

url = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

    files = {
        "images": (
            image.filename,
            image.stream,
            image.mimetype
        )
    }

    response = requests.post(
        url,
        files=files
    )

    health_result = check_health("leaf.jpg")
    return jsonify({
        "results": response.json()["results"],
            "health": health_result
        }
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )
