import topic_distribution
import logging
import show_html
import topic_specific_terms
import main_show_topic_distribution

#serve per stampare anche i log durante la fase di esecuzione
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

list_main_topic = topic_distribution.calculate_main_topic_for_parag()
topic_specific_terms.calculate_specific_terms(list_main_topic)
