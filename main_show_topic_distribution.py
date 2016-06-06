import topic_distribution
import logging
import show_html
import storage


#serve per stampare anche i log durante la fase di esecuzione
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#topic_distribution.load_lda_corpus()
list_main_topic = topic_distribution.calculate_main_topic_for_parag()

#ATTENZIONE: QUANDO DO IL NUMERO DELLA POSIZIONE NON DEVO RIFERIRMI ALL'ATTRIBUTO POS MA ALLA POSIZIONE ALL'INTERO DELLA COLLECTION
cursor = storage.paragraphs_coll.find({'id_story': '../texts/fpn-andrews-andrews.txt', 'pos':8}, {'_id':0,'descr':1})
string = ""
for k in cursor:
    string = k['descr']

show_html.handle_htmlpage(string, list_main_topic[7])


print("Processo terminato.")