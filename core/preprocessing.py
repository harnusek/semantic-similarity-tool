# -*- coding: utf-8 -*-

import requests

def tokenize(sent):
    response = requests.post(url='http://text.fiit.stuba.sk:8080/lematizer/services/lemmatizer/lemmatize/fast', data=sent.encode('utf-8'))
    str = response.content.decode("utf-8")
    return str.split(' ')
