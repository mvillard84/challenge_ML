import flask
from flask import request, jsonify
import json
import time

app = flask.Flask(__name__)

FECHA = time.strftime("%Y%m%d")


# Funcion que recive los valores enviados por el agente, los serializa 
# y los almacena en un archivo json ip_aaaammdd.json
def save_info(args):
    informacion = {
        "ip": "",
        "procesador": "",
        "procesos": "",
        "sesiones": "",
        "so": "",
        "version": ""
    }

    ip = request.args.get('ip', '')
    procesador = request.args.get('procesador', '')
    procesos = request.args.get('procesos', '')
    sesiones = request.args.get('sesiones', '')
    so = request.args.get('so', '')
    version = request.args.get('version', '')

    informacion.update({"ip": ip})
    informacion.update({"procesador": procesador})
    informacion.update({"procesos": procesos})
    informacion.update({"sesiones": sesiones})
    informacion.update({"so": so})
    informacion.update({"version": version})

    with open(informacion['ip'] + '_' + FECHA + '.json', 'w') as outfile:
        json.dump(informacion, outfile)

    return 1


# Main
@app.route('/', methods=['GET'])
def home():
    return "Welcome to server audit"

# Recurso principal hacia donde debe ser enviada la información
@app.route('/audit', methods=['GET'])
def check():
    headers = request.headers
    save_info(request.args)

    return jsonify({"result": "success"}), 200


app.run(debug=True, host='0.0.0.0')
