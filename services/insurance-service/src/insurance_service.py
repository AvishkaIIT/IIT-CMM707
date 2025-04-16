from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded insurance data
insurances = [
    {
        "insurance_id": 1,
        "agent_id": 101,
        "insurance_apply_date": "2024-12-30T10:00:00",
        "insurance_type": "Vehicle",
        "insurance_amount": "LKR2000000"
    },
    {
        "insurance_id": 2,
        "agent_id": 102,
        "insurance_apply_date": "2024-12-31T11:00:00",
        "insurance_type": "Life",
        "insurance_amount": "LKR500000"
    }
]

@app.route("/insurances/", methods=["GET"])
def get_all_insurances():
    return jsonify(insurances)

@app.route("/insurances/<int:insurance_id>", methods=["GET"])
def get_insurance(insurance_id: int):
    if insurance_id < len(insurances):
        return jsonify(insurances[insurance_id])
    return jsonify({"error": "Insurance not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)
