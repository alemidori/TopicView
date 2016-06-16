import topic_distribution
import logging
import show_html

#serve per stampare anche i log durante la fase di esecuzione
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#topic_distribution.load_lda_corpus()
list_main_topic = topic_distribution.calculate_main_topic_for_parag()
#show_html.create_tablesfile()
show_html.fill_tablesfile(list_main_topic)

print("Processo terminato.")