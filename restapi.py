from flask import Flask, jsonify, request, render_template
from monitor import monitor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/processes', methods=['GET'])
def get_processes():
    sort_by = request.args.get('sort_by', 'pid')
    order = request.args.get('order', 'asc')
    filter_name = request.args.get('filter', '').lower()

    data = monitor.process_data
    if filter_name:
        data = [p for p in data if filter_name in p['name'].lower()]

    data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=(order == 'desc'))
    return jsonify(data)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
