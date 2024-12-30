from flask import Flask, jsonify, request

app = Flask(__name__)

appointments = []

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments)

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    appointment = {
        "id": len(appointments) + 1,
        "patient": data["patient"],
        "doctor": data["doctor"],
        "time": data["time"]
    }
    appointments.append(appointment)
    return jsonify(appointment), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
