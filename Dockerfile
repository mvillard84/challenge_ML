FROM python:3

# Instala dependencias
RUN pip install --upgrade pip
RUN pip install flask


# Copia el audit_server.py al directorio especifico
RUN mkdir /audit_server
ADD  audit_server.py /audit_server

# Ejecuta el audit_server
WORKDIR /audit_server
CMD python audit_server.py
