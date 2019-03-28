#!/bin/sh
echo 'Downloading python packages.'	
pip install flask
pip install connexion
pip install swagger-ui-bundle
pip install lxml
pip install "requests[security]"
# pip install pyopenssl ndg-httpsclient pyasn1
# pip install nltk
# ---
# echo 'Running unit tests.'
./tests/test.sh
# ---
echo 'Opening browser.'	
python -mwebbrowser http://localhost:5000/
# ---
echo 'Starting server.'	
python api/server.py
