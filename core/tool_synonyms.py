import time
from lxml import html
import requests
from lxml.etree import tostring

def get_similarity(sent1,sent2):
    return synonym_list(sent1)

def synonym_list(word):
    url = 'https://slovnik.azet.sk/synonyma/?q=' + word
    page = requests.get(url)
    tree = html.fromstring(page.content)
    elems = tree.xpath('//em[@class="term"]')
    terms = [e.text_content() for e in elems]
    return terms
