from flask import Flask, Blueprint, request, jsonify
from networkinfo import Ipinfo
from portchecker import Checkport
import os

app_bp = Blueprint('api', __name__, url_prefix='/api')

@app_bp.route('/', methods=['GET'])
def greeting():
    return jsonify({"message": "Welcome to the personal assistant api!"}), 200

@app_bp.route('/ipinfo', methods=['GET'])
def ipInfo():
    try:
        ipinfo_obj = Ipinfo(request.remote_addr)
        ipinfo = ipinfo_obj.getInfo()
        return jsonify({"ip": ipinfo['ip'], "city": ipinfo['city'], "country": ipinfo['country']}), 200
    except Exception as error:
        return str(error), 500

@app_bp.route('/ipinfo/<ip>', methods=['GET'])
def externalipInfo(ip):
    try: 
        externalipinfo_obj = Ipinfo(ip)
        ipinfo = externalipinfo_obj.getInfo()
        return jsonify({"ip": ipinfo['ip'], "city": ipinfo['city'], "country": ipinfo['country']}), 200
    except Exception as error:
        return str(error), 500

@app_bp.route('/portchecker', methods=['GET'])
def local_portChecker():
    ip = request.args.get('ip')
    port = request.args.get('port')
    if ip is None or port is None:
        return jsonify({"error": "Please provide both 'ip' and 'port' parameters in the endpoint."}), 400
    try:
        port = int(port)
    except ValueError:
        return jsonify({"error": "Port must be an integer."}), 400
    checker = Checkport(ip=ip, port=port)
    try:
        result = checker.portChecker()
        return jsonify(result), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(app_bp)
    host = os.environ.get('HOST')
    port = int(os.environ.get('PORT')) 
    app.run(debug=True, host=host, port=port)

