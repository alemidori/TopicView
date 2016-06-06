from html.parser import HTMLParser
from bs4 import BeautifulSoup
import random
import storage


html_path = "prova.html"

def handle_htmlpage(left, right):

    map_color = set_topic_random_color()

    color = "#%06x" % random.randint(0, 0xFFFFFF) #genera un colore random (per provare per quando dovro' darlo ai topic)

    #serve a parsare l'html e a modificare i contenuti dei tag e gli eventuali attributi
    soup = BeautifulSoup(open(html_path), 'lxml')
    contenuto = soup.p #mi riferisco al paragrafo dell'html attraverso il tag 'p'

    # modifico il contenuto del tag con una nuova stringa
    contenuto.string =  left
    contenuto['style'] = "background-color:"+map_color[right]+";color:white"
    topic = soup.h1
    topic.string = str(right)
    topic['style'] = "background-color:"+map_color[right]+";color:white"


    with open(html_path, "wb") as prova:
        prova.write(soup.prettify("utf-8"))

    return


def set_topic_random_color():
    map_topic_color = {}

    color = "#%06x" % random.randint(0, 0xFFFFFF)  # colore random

    for i in range(100):
        map_topic_color[i] = color

    return map_topic_color



with open(html_path, "r") as prova:
    print(prova.read())