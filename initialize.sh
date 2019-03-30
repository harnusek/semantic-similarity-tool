#!/bin/sh
# echo 'Running unit tests.'
cd ./tests/
./test.sh
cd ..
# ---
echo 'Opening browser.'	
python -mwebbrowser http://localhost:5000/
# ---
echo 'Starting server.'	
python api/server.py
