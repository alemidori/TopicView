from html.parser import HTMLParser
from bs4 import BeautifulSoup
import random

html_path = "../../prova.html"

def handle_htmlpage():

    color = "#%06x" % random.randint(0, 0xFFFFFF) #genera un colore random (per provare per quando dovro' darlo ai topic)

    #serve a parsare l'html e a modificare i contenuti dei tag e gli eventuali attributi
    soup = BeautifulSoup(open(html_path), 'lxml')
    tag = soup.p #mi riferisco al paragrafo dell'html attraverso il tag 'p'
    tag.string = "madonnaaaaaa" #modifico il contenuto del tag con una nuova stringa
    tag['style'] = "background-color:"+color+";color:white"

    with open(html_path, "wb") as prova:
        prova.write(soup.prettify("utf-8"))

    return

handle_htmlpage()

with open(html_path, "r") as prova:
    print(prova.read())