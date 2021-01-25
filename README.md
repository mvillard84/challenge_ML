**Instrucciones**

*Ejecutar el audit_server:*

- python audit_server.py

*Ejecutar el audit_server utilizando Docker*

- docker build -f Dockerfile -t audit_server . docker run -p 5001:5000 audit_server

*Ejecutar el audit_agent en cada uno de los host a revisar:*

- python agent.py

*Para que la herrramienta de auditoria se ejecute constantemente se debe configurar en el servidor el script audit_server.py para que corra en segundo plano
y en el/los host, se debe crear un cron asociado al audit_agent.py para que se ejecute bajo la frecuencia deseada*
