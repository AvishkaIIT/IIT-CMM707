from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/bills', methods=['GET'])
def get_bills():
    bills = [
        {"bill_id": 1, "amount": 1500, "status": "Paid"},
        {"bill_id": 2, "amount": 3800, "status": "Unpaid"},
        {"bill_id": 3, "amount": 2300, "status": "Paid"}
    ]
    return jsonify(bills)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
