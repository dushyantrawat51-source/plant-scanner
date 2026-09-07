import random

def check_health(image_path):

    results = [

        {
            "health": "Healthy",
            "disease": "None",
            "confidence": 95,
            "suggestion": "Plant appears healthy."
        },

        {
            "health": "Diseased",
            "disease": "Leaf Spot",
            "confidence": 91,
            "suggestion": "Apply fungicide."
        },

        {
            "health": "Diseased",
            "disease": "Powdery Mildew",
            "confidence": 89,
            "suggestion": "Improve air circulation."
        }

    ]

    return random.choice(results)
