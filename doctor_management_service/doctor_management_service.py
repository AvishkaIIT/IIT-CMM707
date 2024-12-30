from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for doctors
doctors = [
    {"doctor_id": 1, "name": "Dr. Alice", "specialization": "Cardiology"},
    {"doctor_id": 2, "name": "Dr. Bob", "specialization": "Neurology"},
    {"doctor_id": 3, "name": "Dr. Charlie", "specialization": "Orthopedics"}
]

@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify(doctors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
