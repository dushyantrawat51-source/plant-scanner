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
    print("FILES:", request.files)

    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        })

    image = request.files["image"]

    url = (
        f"https://my-api.plantnet.org/"f"v2/identify/all?api-key={API_KEY}"
    )

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
