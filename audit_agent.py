import subprocess
import requests as rq


def get_info():
    informacion = []
    # Obtiene ip del host
    ip = subprocess.check_output(['hostname', '-I'])
    informacion.append(ip.decode("utf-8"))
    # Obtiene procesador del host
    procesador = subprocess.check_output(['uname', '-p'])
    informacion.append(procesador.decode("utf-8"))
    # Obtiene procesos en ejecucion en el host
    procesos = subprocess.check_output('ps')
    informacion.append(procesos.decode("utf-8"))
    # Obtiene sesiones iniciadas en el host
    sesiones = subprocess.check_output('who')
    informacion.append(sesiones.decode("utf-8"))
    # Obtiene SO del host
    so = subprocess.check_output('uname')
    informacion.append(so.decode("utf-8"))
    # Obtiene version del SO del host
    version = subprocess.check_output(['uname', '-o'])
    informacion.append(version.decode("utf-8"))

    return informacion


informacion = get_info()

# Arma la url de la API del audit_server
url = "http://127.0.0.1:5000/audit?ip=" + informacion[0] + "&procesador=" + informacion[1] + "&procesos=" + \
      informacion[2] + "sesiones=" + informacion[3] + "&so=" + informacion[4] + "&version=" + informacion[5] + '"'

payload = {}
headers = {}

# Envia el request response al audit_server
response = rq.request("GET", url, headers=headers, data=payload)
print(response.text)
