from flask import Flask, jsonify, request
app = Flask(__name__)

reports = []

@app.route("/report", methods=["POST"])
def add_report():
    data = request.json
    reports.append(data)
    return jsonify({"status": "success"})

@app.route("/reports", methods=["GET"])
def get_reports():
    return jsonify(reports)

if __name__ == "__main__":
    app.run(debug=True)
