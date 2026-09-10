from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "2b10rk4sO14ZfS4OXo4lVgyJe"

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
            image.read(),
            image.mimetype
        )
    }

    try:

        response = requests.post(url, files=files)
        data = response.json()

        if len(data.get("results", [])) == 0:
            return jsonify({
                "plant_name": "Unknown",
                "scientific_name": "Unknown",
                "confidence": 0
            })

        best_match = data["results"][0]

        plant_name = "Unknown"

        if best_match["species"].get("commonNames"):
            plant_name = best_match["species"]["commonNames"][0]

        scientific_name = best_match["species"].get(
            "scientificNameWithoutAuthor",
            "Unknown"
        )

        confidence = round(best_match["score"] * 100, 2)

        return jsonify({
            "plant_name": plant_name,
            "scientific_name": scientific_name,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
