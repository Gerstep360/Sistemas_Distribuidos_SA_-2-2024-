from flask import Flask, request, jsonify, render_template_string
import socket

app = Flask(__name__)


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
       
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

@app.route('/')
def index():
    local_ip = get_local_ip()
    with open('Tarea#1 (Rest)\index.html', 'r') as file:
        html_content = file.read().replace("{{LOCAL_IP}}", local_ip)
        return render_template_string(html_content)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!"), 200

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    if not data:
        return jsonify(message="No data provided"), 400
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
