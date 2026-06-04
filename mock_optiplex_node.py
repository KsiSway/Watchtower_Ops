from flask import Flask, request, jsonify
import logging

# Disable Flask default logging for cleaner C2 output
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Mock high-performance NPU inference
    return jsonify({
        "node": "OPTIPLEX",
        "transport": "HTTP",
        "status": "COMPLETED",
        "result": "OBJECT_DETECTED",
        "confidence": 0.98
    })

if __name__ == '__main__':
    print("[*] Watchtower Mock OptiPlex Server active on port 8081")
    app.run(port=8081, debug=False)
