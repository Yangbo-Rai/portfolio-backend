import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_info():
    return jsonify({
        "name": "Yangbo Rai",
        "title": "Full Stack Developer",
        "specialization": "Front-end Technology"
    })

@app.route('/api/info')
def get_info():
    return jsonify({
        "name": "Yangbo Rai",
        "title": "Full Stack Developer",
        "specialization": "Front-end Technology"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
