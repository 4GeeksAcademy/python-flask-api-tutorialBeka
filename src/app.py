
from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {
        "label": "Sample", 
        "done": True
    },
    {
        "label": "Sample", 
        "done": False
    },
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

