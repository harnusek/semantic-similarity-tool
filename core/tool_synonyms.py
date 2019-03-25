import time
from lxml import html
import requests
from lxml.etree import tostring

def get_similarity(sent1,sent2):
    return list_synonym(sent1)

def list_synonym(word):
    url = 'https://slovnik.azet.sk/synonyma/?q=' + word
    page = requests.get(url)
    tree = html.fromstring(page.content)
    terms = tree.xpath('//em[@class="term"]')
    return [t.text_content() for t in terms]
