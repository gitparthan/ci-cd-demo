
from flask import Flask, render_template, request, jsonify
from calculator import add

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/add")
def add_numbers():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON input"}), 400

    a = data.get("a")
    b = data.get("b")

    if type(a) not in (int, float) or type(b) not in (int, float):
        return jsonify({"error": "Both values must be numbers"}), 400

    return jsonify({"result": add(a, b)})

if __name__ == "__main__":
    app.run(debug=True)
