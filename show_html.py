from bs4 import BeautifulSoup
import random
import storage
import specificity

html_file = "index.html"

soup_html = BeautifulSoup(open(html_file), 'lxml')
map_topic_color = {}

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
        #print("Apro racconto "+str(stories.index(p)))
        cursor = storage.paragraphs_coll.find({'id_story': p}, {'_id': 0, 'descr': 1, 'tokens':1})

        strings = []
        paragtokens = []

        for k in cursor:
            strings.append(k['descr'])
            paragtokens.append(k['tokens'])

        for text in strings:
            tokenlist = paragtokens[strings.index(text)]
            print("Scrittura paragrafo " + str(strings.index(text)) + " / " + str(len(strings)) + " racconto " + str(stories.index(p))+" su "+str(len(stories)))
            listwords = []
            for v in storage.topics_terms.find({'id_topic':listmaintopic[increment_for_topiclist]}, {'_id':0,'words_list':1}):
                listwords = v['words_list'] #lista prime 50 parole del topic date dall'LDA
            #print("Stampo le prime 5 parole specifiche...")
            specific_words = specificity.get_specific_words(listwords, tokenlist)
            specific_words_toshow = []
            if len(specific_words) > 5:
                for n in range(0,5):
                    specific_words_toshow.append(specific_words[n])
            else:
                specific_words_toshow = specific_words

            handle_table(str(p).replace("../texts/", "tables/").replace(".txt", ".html"), text, listmaintopic[increment_for_topiclist], specific_words_toshow)
            increment_for_topiclist += 1
    return



def set_topic_random_color():

    for i in range(100):
        map_topic_color[i] = "#%06x" % random.randint(0, 0xFFFFFF)

    return
