import random

def check_health(image_path):

    disease = "No Disease Detected"

    remedies = {
        "No Disease Detected":
        "Keep regular watering and nutrient management.",

        "Leaf Spot":
        "Use copper fungicide and remove infected leaves.",

        "Powdery Mildew":
        "Improve ventilation and apply sulfur spray.",

        "Rust":
        "Use fungicide and avoid overhead watering.",

        "Blight":
        "Remove affected leaves and apply recommended fungicide."
    }

    return {
        "health": "Healthy",
        "disease": disease,
        "confidence": 95,
        "remedy": remedies[disease]
    }

    return random.choice(results)
