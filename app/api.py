from flask import Flask, request, jsonify
from app.model_handler import make_prediction


app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Service is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        version = request.args.get("v", "v1")
        input_data = request.get_json()

        if input_data is None:
            return jsonify({
                "error": "No JSON data provided"
            }), 400

        result = make_prediction(input_data, version)
        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)