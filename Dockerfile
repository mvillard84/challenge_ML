FROM python:3

# Install Dependencies
RUN pip install --upgrade pip
RUN pip install flask


# Place audit_server
RUN mkdir /audit_server
ADD  audit_server.py /audit_server

# Runs audit_server
WORKDIR /audit_server
CMD python audit_server.py
