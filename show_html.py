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
    table = soup.find('table', attrs={'id': 'topicshow'} )
    #contenuto = soup.find('td', attrs={'id': 'textcontent'})
    newrow = soup.new_tag("tr")

    contenuto = soup.new_tag("td")
    newrow.append(contenuto)

    tag_p = soup.new_tag("p")
    contenuto.append(tag_p)
    tag_p.string = left
    # modifico il contenuto del tag con una nuova stringa
    tag_p['style'] = "background-color:"+map_color[right]+";color:white"

    #topic_side = soup.find('td', attrs={'id': 'topictext'})
    topic_side = soup.new_tag("td")
    newrow.append(topic_side)
    tag_h1 = soup.new_tag("h1")
    topic_side.append(tag_h1)

    tag_h1.string = "Topic numero " + str(right)
    tag_h1['style'] = "background-color:"+map_color[right]+";color:white"

    table.append(newrow)

    with open(html_path, "wb") as prova:
        prova.write(soup.prettify("utf-8"))

    return


def set_topic_random_color():
    map_topic_color = {}

    color = "#%06x" % random.randint(0, 0xFFFFFF)  # colore random

    for i in range(100):
        map_topic_color[i] = color

    return map_topic_color
