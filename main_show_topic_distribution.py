import topic_distribution
import logging


#serve per stampare anche i log durante la fase di esecuzione
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

topic_distribution.load_lda_corpus()


print("Processo terminato.")