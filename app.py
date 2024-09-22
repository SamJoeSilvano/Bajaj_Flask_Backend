from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os

app = Flask(__name__)
CORS(app)

# GET Endpoint
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({
        "operation_code": 1
    }), 200

# POST Endpoint
@app.route('/bfhl', methods=['POST'])
def process_request():
    data = request.json.get('data', [])
    print(data)
    file_b64 = request.json.get('file_b64', None)
    
    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    # Find highest lowercase alphabet
    lowercase_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None
    
    # File processing
    file_valid = False
    file_mime_type = None
    file_size_kb = None
    
    if file_b64:
        try:
            file_data = base64.b64decode(file_b64)
            file_valid = True
            file_mime_type = 'application/octet-stream'  # Modify according to actual MIME type
            file_size_kb = len(file_data) / 1024
        except Exception:
            file_valid = False

    # Response
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)

