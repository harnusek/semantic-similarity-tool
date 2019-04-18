# semantic-similarity-tool 
## A tool for determining the semantic similarity of texts

### Required sources:
```
core/sources/[SK]prim-6.1-public-all.shuffled.080cbow.bin
core/sources/stop_words_SK.txt
```


### For the first start run `initialize.sh` script:
```
echo 'Installing requirements.'
pip install -r requirements.txt

echo 'Running unit tests.'
cd ./tests/
./test.sh
cd ..

echo 'Opening browser.'	
python -mwebbrowser http://localhost:5000/

echo 'Starting server.'	
python api/server.py
```
