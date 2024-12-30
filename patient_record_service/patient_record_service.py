from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/patients', methods=['GET'])
def get_patients():
    patients = [{"id": 1, "name": "Mary"}, {"id": 2, "name": "John"}]
    return jsonify(patients)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)