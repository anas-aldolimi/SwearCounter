from flask import Flask, request, jsonify

app = Flask(__name__)

scores = {"Aldo": 0, "Hittori": 0}


@app.route("/get_scores", methods=["GET"])
def get_scores():
  return jsonify(scores)


@app.route("/update_score", methods=["POST"])
def update_score():
  data = request.get_json()
  scores["Aldo"] = data.get("Aldo", scores["Aldo"])
  scores["Hittori"] = data.get("Hittori", scores["Hittori"])
  return jsonify({"message": "Score updated successfully"})


if __name__ == "__main__":
  app.run()
