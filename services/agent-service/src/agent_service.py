from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded agent data
agents = [
    {
        "agent_id": 1,
        "name": "John Doe",
        "age": 30,
        "gender": "Male",
        "agent_branch": ["Kandy"],
        "products": ["Life", "Vehicle"]
    },
    {
        "agent_id": 2,
        "name": "Jane Smith",
        "age": 25,
        "gender": "Female",
        "medical_history": ["Colombo"],
        "prescriptions": ["Vehicle"]
    }
]

@app.route("/agents/", methods=["GET"])
def get_agents():
    return jsonify(agents)

@app.route("/agents/<int:agent_id>", methods=["GET"])
def get_agent(agent_id: int):
    agent = next((p for p in agents if p["agent_id"] == agent_id), None)
    if agent:
        return jsonify(agent)
    return jsonify({"error": "agent not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
