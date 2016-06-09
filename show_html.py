from bs4 import BeautifulSoup
import random
import storage
import glob

html_file = "index.html"

soup_html = BeautifulSoup(open(html_file), 'lxml')
map_topic_color = {}

#todo: questa funzione diventera' handle_tables perche' devo riempire tanti html quanti sono i file txt
#IN PRATICA: fare una query in modo che per ogni diverso file si ricostruisca il contenuto e gli si associno i valori
#dei topic corrispondenti alla posizione del record in mongodb (ancora da vedere)
def handle_table(pathfile,left, topicnum,listwords):

    soup_table = BeautifulSoup(open(pathfile), 'lxml')
    table = soup_table.find('table', attrs={'id': 'topicshow'} )
    newrow = soup_table.new_tag("tr")

    contenuto = soup_table.new_tag("td")
    newrow.append(contenuto)

    tag_p = soup_table.new_tag("p")
    contenuto.append(tag_p)
    tag_p.string = left
    # modifico il contenuto del tag con una nuova stringa
    tag_p['style'] = "background-color:"+map_topic_color[topicnum]+";color:white"

    topic_side = soup_table.new_tag("td")
    newrow.append(topic_side)
    tag_p2 = soup_table.new_tag("p")
    topic_side.append(tag_p2)

    tag_p2.string = "Topic numero " + str(topicnum) + " Parole chiave: " \
                    + listwords[0] + " " + listwords[1] + " " + listwords[2]
    tag_p2['style'] = "background-color:"+map_topic_color[topicnum]+";color:white"

    table.append(newrow)

    with open(pathfile, "wb") as prova:
        prova.write(soup_table.prettify("utf-8"))

    return

def create_tablesfile():

    html_file_list = []

    for k in storage.paragraphs_coll.distinct('id_story'):
         html_file_list.append(str(k).replace("../texts/", "").replace(".txt",".html"))

    for n in html_file_list:
        with open("tables/"+n, "w") as file:
            file.write("<html><body><table id='topicshow' style='padding:0%;margin:0%' with='100%'><tr><td id='textcontent' width='50%'></td><td id='topictext' width='50%'></td></tr></table></body></html>")

    return

def fill_tablesfile(listmaintopic):

    set_topic_random_color()

    stories = []

    increment_for_topiclist = 0

    for k in storage.paragraphs_coll.distinct('id_story'):
        stories.append(k)

    for p in stories:
        print("Apro racconto "+str(stories.index(p)))
        cursor = storage.paragraphs_coll.find({'id_story': p}, {'_id': 0, 'descr': 1})

        strings = []
        for k in cursor:
            strings.append(k['descr'])

        for text in strings:
            print("Scrittura paragrafo " + str(strings.index(text)) + " / " + str(len(strings)))
            listwords = []
            for v in storage.topics_terms.find({'id_topic':listmaintopic[increment_for_topiclist]}, {'_id':0,'words_list':1}):
                listwords = v['words_list']
            handle_table(str(p).replace("../texts/", "tables/").replace(".txt", ".html"), text, listmaintopic[increment_for_topiclist], listwords)
            increment_for_topiclist += 1
    return

def set_topic_random_color():

    for i in range(100):
        map_topic_color[i] = "#%06x" % random.randint(0, 0xFFFFFF)

    return

