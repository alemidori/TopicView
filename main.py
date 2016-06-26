import splitting
import terms_dictionary
import logging
import storage

#serve per stampare anche i log durante la fase di esecuzione
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#chiamo il metodo che processa tutti i file dividendoli
#in paragrafi e applicando rimozione stopword rimozione
#punteggiatura e stemming
splitting.process_stories()

terms_dictionary.create_terms_dictonary() #creo dizionario dei termini di tutti i file

storage.save_frequency_allcorpus()

print("Collezioni create. Processo terminato.")