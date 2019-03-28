# -*- coding: utf-8 -*-

import preprocessing
from lxml import html
import requests
from lxml.etree import tostring

def get_similarity(sent1,sent2):
    """
    Return similarity koeficient
    """
    tokens1 = preprocessing.tokenize(sent1)
    tokens2 = preprocessing.tokenize(sent2)
    return sim_by_matrix(tokens1, tokens2)

def synonym_list(word):
    url = 'https://slovnik.azet.sk/synonyma/?q=' + word
    page = requests.get(url)
    tree = html.fromstring(page.content)
    elems = tree.xpath('//em[@class="term"]')
    terms = [e.text_content() for e in elems]
    return terms

def sim_by_matrix(xList, yList):
    points = 0
    for x in xList:
        for y in yList:
            points = points + sim_by_tokens(x,y)
    return points

def sim_by_tokens(x,y):
    if any(elem in synonym_list(x) for elem in synonym_list(y)):
        return 1
    else:
        return 0