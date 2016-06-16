import splitting
import terms_dictionary
import logging

#serve per stampare anche i log durante la fase di esecuzione
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

splitting.process_stories()

terms_dictionary.create_terms_dictonary()




print("Collezioni create. Processo terminato.")