from bs4 import BeautifulSoup
import random
import storage

html_path = "prova.html"
soup = BeautifulSoup(open(html_path), 'lxml')

def handle_table(left, right):

    map_color = set_topic_random_color()

    color = "#%06x" % random.randint(0, 0xFFFFFF) #genera un colore random

    #serve a parsare l'html e a modificare i contenuti dei tag e gli eventuali attributi

    table = soup.find('table', attrs={'id': 'topicshow'} )
    newrow = soup.new_tag("tr")

    contenuto = soup.new_tag("td")
    newrow.append(contenuto)

    tag_p = soup.new_tag("p")
    contenuto.append(tag_p)
    tag_p.string = left
    # modifico il contenuto del tag con una nuova stringa
    tag_p['style'] = "background-color:"+map_color[right]+";color:white"

    topic_side = soup.new_tag("td")
    newrow.append(topic_side)
    tag_h1 = soup.new_tag("h1")
    topic_side.append(tag_h1)

    tag_h1.string = "Topic numero " + str(right)
    tag_h1['style'] = "background-color:"+map_color[right]+";color:white"

    table.append(newrow)

    return


def handle_jquery(list_topic):
    file_list = []
    div_list = soup.find('div')

    cursor = storage.paragraphs_coll.distinct('id_story')
    #cursor2 = storage.paragraphs_coll.find({'id_story': '../texts/fpn-andrews-andrews.txt'}, {'_id': 0, 'descr': 1})

    for k in storage.paragraphs_coll.distinct('id_story'):
        file_list.append(k)

    for k in cursor:
        print(k)
        tag_p = soup.new_tag("p")
        tag_p['style'] = "cursor:pointer"
        tag_p.string = k
        div_list.append(tag_p)

    # strings = []
    # for k in cursor2:
    #     strings.append(k['descr'])
    #
    # for text in strings:
    #     print("Scrittura paragrafo " + str(strings.index(text)) + " / " + str(len(strings)))
    #     handle_table(text, list_topic[strings.index(text)])

    with open(html_path, "wb") as prova:
        prova.write(soup.prettify("utf-8"))
    return


def set_topic_random_color():
    map_topic_color = {}

    color = "#%06x" % random.randint(0, 0xFFFFFF)  # colore random

    for i in range(100):
        map_topic_color[i] = color

    return map_topic_color

