# -*- coding: utf-8 -*-

import preprocessing
from lxml import html
import requests
from lxml.etree import tostring

def get_similarity(sent1,sent2):
    """
    Return similarity between two sentences
    """
    tokens1 = preprocessing.tokenize(sent1)
    tokens2 = preprocessing.tokenize(sent2)
    synonyms1 = synonym_list(tokens1)
    synonyms2 = synonym_list(tokens2)
    matrix = synonym_matrix(tokens1, tokens2)
    return sim_by_matrix(tokens1, tokens2)

def synonym_list(tokens):
    """
    Return list of synonyms for each token
    """
    list = []
    for token in tokens:
        url = 'https://slovnik.azet.sk/synonyma/?q=' + token
        page = requests.get(url)
        tree = html.fromstring(page.content)
        elems = tree.xpath('//em[@class="term"]')
        terms = [e.text_content() for e in elems]
        list.append(terms)
    return list

def synonym_matrix(synonyms1, synonyms2):
    pass


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