from flask import Flask, request, jsonify

app = Flask(__name__)

sensor_data = {"temperature": 0, "humidity": 0}

@app.route('/data', methods=['POST'])
def receive_data():
    global sensor_data
    data = request.json
    sensor_data = data
    return jsonify({"message": "Data received"}), 200

@app.route('/get_data', methods=['GET'])
def send_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
