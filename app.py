from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    current_time = datetime.now().isoformat()
    return jsonify(message="Hello, World!", timestamp=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
