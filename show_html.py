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

    #visualizzare un racconto alla volta ricostruito partendo dalle posizioni nella collezione
    #utilizzare un percentile per scremare i topic più rilevanti per un paragrafo
    #associare ad ogni topic un colore randomico
    #mostrare l'intero testo e sotto ogni paragrafo il colore del topic più rilevante
    #mostrare in corrispondenza dei topic: il colore, il livello di presenza nell'intero racconto
    #e la posizione all'interno del racconto stesso

    #IN PRATICA
    #prendi il massimo tra i valori della distribuzione dei documenti sui topic nella coppia(secondo valore) e
    #inserisci in un array il valore dell'id del paragrafo e l'id del topic con  valore massimo
    #effettuare un'interrogazione per cui per ogni documento txt si prende il testo vero e proprio
    #sotto la voce "descr" e lo si visualizza ...
    return

handle_htmlpage()

with open(html_path, "r") as prova:
    print(prova.read())