from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/send_notification/", methods=["POST"])
def send_notification():
    # Hardcoded notification data
    corporate_email = "corporate@example.com"
    subject = "Sales target achievement"
    message = "Dear all, this is to notify that your sales target is achieved!"

    # Simulating sending email (no actual sending here)
    return jsonify({
        "status": "Notification sent",
        "to": corporate_email,
        "subject": subject,
        "message": message
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8002)