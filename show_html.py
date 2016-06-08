from bs4 import BeautifulSoup
import random
import storage

html_path = "fpn-andrews-andrews.html"
html_file = "prova.html"
soup_table = BeautifulSoup(open(html_path), 'lxml')
soup_html = BeautifulSoup(open(html_file), 'lxml')


#todo: questa funzione diventera' handle_tables perche' devo riempire tanti html quanti sono i file txt
#IN PRATICA: fare una query in modo che per ogni diverso file si ricostruisca il contenuto e gli associno i valori
#dei topic corrispondenti alla posizione del record in mongodb (ancora da vedere)
def handle_table(left, right):

    map_color = set_topic_random_color()

    table = soup_table.find('table', attrs={'id': 'topicshow'} )
    newrow = soup_table.new_tag("tr")

    contenuto = soup_table.new_tag("td")
    newrow.append(contenuto)

    tag_p = soup_table.new_tag("p")
    contenuto.append(tag_p)
    tag_p.string = left
    # modifico il contenuto del tag con una nuova stringa
    tag_p['style'] = "background-color:"+map_color[right]+";color:white"

    topic_side = soup_table.new_tag("td")
    newrow.append(topic_side)
    tag_h1 = soup_table.new_tag("h1")
    topic_side.append(tag_h1)

    tag_h1.string = "Topic numero " + str(right)
    tag_h1['style'] = "background-color:"+map_color[right]+";color:white"

    table.append(newrow)

    return


def handle_jquery(list_topic):

    file_list = []
    div_list = soup_html.find('div')

    cursor = storage.paragraphs_coll.distinct('id_story')
    cursor2 = storage.paragraphs_coll.find({'id_story': '../texts/fpn-andrews-andrews.txt'}, {'_id': 0, 'descr': 1})

    for k in storage.paragraphs_coll.distinct('id_story'):

        file_list.append(str(k).replace("../texts/", "").replace(".txt",".html"))

    for k in file_list:

        print(k)
        tag_p = soup_html.new_tag("p")
        tag_p['style'] = "cursor:pointer"
        tag_p.string = k
        div_list.append(tag_p)


    strings = []
    for k in cursor2:
        strings.append(k['descr'])
    #
    # for text in strings:
    #     print("Scrittura paragrafo " + str(strings.index(text)) + " / " + str(len(strings)))
    #     handle_table(text, list_topic[strings.index(text)])


    with open(html_path, "wb") as prova:
        prova.write(soup_table.prettify("utf-8"))

    with open(html_file, "wb") as prova:
        prova.write(soup_html.prettify("utf-8"))

    return


def set_topic_random_color():
    map_topic_color = {}

    color = "#%06x" % random.randint(0, 0xFFFFFF)  # colore random

    for i in range(100):
        map_topic_color[i] = color

    return map_topic_color

