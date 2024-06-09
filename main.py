from flask import Flask, Blueprint, request, jsonify
from networkinfo import Ipinfo
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
    
if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(app_bp)
    host = os.environ.get('HOST')
    port = int(os.environ.get('PORT')) 
    app.run(debug=True, host=host, port=port)

