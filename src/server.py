from flask import Flask, request, jsonify
from gamification import complete_task

app = Flask(__name__)

@app.route('/biometric-data', methods=['POST'])
def biometric_data():
    data = request.json
    # Process biometric data here
    return jsonify({"status": "success", "data": data})

@app.route('/complete-task', methods=['POST'])
def complete_task_route():
    task = request.json
    result = complete_task(task)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
