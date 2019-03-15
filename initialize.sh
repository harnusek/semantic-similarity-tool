#!/bin/sh
echo 'Downloading python packages.'	
pip install flask
pip install connexion
pip install swagger-ui-bundle
echo 'Opening browser.'	
python -mwebbrowser http://0.0.0.0:5000/
echo 'Starting server.'	
python server.py
