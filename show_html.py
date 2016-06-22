from bs4 import BeautifulSoup
import random
import storage
import specificity

html_file = "htmls/index.html"

soup_html = BeautifulSoup(open(html_file), 'lxml')
map_topic_color = {}

def create_tablesfile():

    html_file_list = []

    for k in storage.paragraphs_coll.distinct('id_story'):
         html_file_list.append(str(k).replace("../texts/", "").replace(".txt",".html"))

    for n in html_file_list:
        with open("htmls/tables/"+n, "w") as file:
            file.write("<html><body><table id='topicshow' style='padding:0%;margin:0%' with='100%'><tr><td id='textcontent' width='50%'></td><td id='topictext' width='50%'></td></tr></table></body></html>")

    return

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

    tag_p2.string = "Topic numero " + str(topicnum) + " Parole chiave: " + str(listwords)

    tag_p2['style'] = "background-color:"+map_topic_color[topicnum]+";color:white"

    table.append(newrow)

    with open(pathfile, "wb") as prova:
        prova.write(soup_table.prettify("utf-8"))

    return

def fill_tables(doc,text,topic,finallisttoshow):

    stories = []
    for k in storage.paragraphs_coll.distinct('id_story'):
        stories.append(k)

    handle_table(str(doc).replace("../texts/", "htmls/tables/").replace(".txt", ".html"), text,
                 topic, finallisttoshow)

    return

def fill_topicfile(topic,termslist):

    pathfile = "htmls/topic.html"
    soup_table = BeautifulSoup(open(pathfile), 'lxml')
    table = soup_table.find('table', attrs={'id': 'topiclist'})
    newrow = soup_table.new_tag("tr")

    contenuto = soup_table.new_tag("td")
    newrow.append(contenuto)

    contenuto['class'] = "space"
    tag_p = soup_table.new_tag("p")
    contenuto.append(tag_p)
    tag_p.string = str(topic)
    # modifico il contenuto del tag con una nuova stringa
    tag_p['style'] = "background-color:" + map_topic_color[topic] + ";color:white"
    tag_p['class'] = "customfontleft"

    topic_side = soup_table.new_tag("td")
    topic_side['class'] = "space"
    newrow.append(topic_side)
    tag_p2 = soup_table.new_tag("p")
    topic_side.append(tag_p2)

    tag_p2.string = str(termslist)
    tag_p2['style'] = "background-color:" + map_topic_color[topic] + ";color:white"
    tag_p2['class'] = "customfontright"

    table.append(newrow)

    with open(pathfile, "wb") as prova:
        prova.write(soup_table.prettify("utf-8"))

    return

def add_docrow_in_topic_description(doc_num):

    pathfile = "htmls/topic.html"
    soup_table = BeautifulSoup(open(pathfile), 'lxml')
    table = soup_table.find('table', attrs={'id': 'topiclist'})
    tr = soup_table.new_tag("tr")
    td = soup_table.new_tag("td")
    tr.append(td)
    td['class'] = "docdiv"
    p = soup_table.new_tag("p")
    p['class'] = "customfontleft"
    p.string = "Documento "+str(doc_num)
    td.append(p)
    table.append(tr)


    with open(pathfile, "wb") as prova:
        prova.write(soup_table.prettify("utf-8"))
    return


def set_topic_random_color():

    for i in range(100):
        map_topic_color[i] = "#%06x" % random.randint(0, 0xFFFFFF)

    return
