from flask import Flask, request, jsonify, render_template
from emotion_detector import analyze_emotion
from formatter import format_output

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotion", methods=["POST"])
def emotion():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        emotions = analyze_emotion(data["text"])

        if emotions is None:
            return jsonify({"error": "Empty input"}), 400

        return jsonify(format_output(emotions))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)