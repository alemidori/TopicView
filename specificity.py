import storage
import cmath
from collections import Counter
from itertools import chain

alltokens = []

def get_specific_words(Ldawords, tokenlist):

    specific_words = []
    final_words_list = []

    #print("1. Conto le occorrenze nella lista di token del paragrafo...")
    # creo un dizionario in cui salvo ogni termine e la sua frequenza nella lista
    term_freqs = Counter(tokenlist)

    #print("2. Per ogni parola dell'Lda calcolo la sua specificità nel paragrafo...")
    for word in Ldawords:
        tf = 0
        tf_all = 1

        if word in term_freqs.keys():
            for t in term_freqs.keys():
                if t == word:
                    tf = term_freqs[t]

            for k in storage.term_frequency_corpus.find({'term': word}, {'_id':0,'frequency':1}):
                tf_all = k['frequency']
            try:
                specificity = (tf - tf_all)/cmath.sqrt(tf_all)

            except KeyError:
                specificity = -1

            if cmath.phase(specificity) > 0.00:
                specific_words.append(word)

    #vado a prendere il termine originale con maggiore occorrenza nella collezione di riferimento per i termini stemmizzati
    for w in specific_words:
        for k in storage.terms_ref_coll.find({'token': w},{'_id':0,'originals':1}):
            counter = Counter(k['originals'])
            mostcomm = counter.most_common(1)[0][0] #perche' restituisce una lista di coppie (term, freq)
            final_words_list.append(mostcomm)

    return final_words_list


def save_frequency_allcorpus():
    print("Sto raccogliendo tutti i token...")
    # salvo una lista con tutte le liste di token di tutti i documenti del corpus in modo da poter calcolare la specificità
    for p in storage.paragraphs_coll.find(None, {'_id': 0, 'tokens': 1}):
        alltokens.append(p['tokens'])

    print("Ho finito di raccogliere i token.")

    print("Conto le occorenze nella lista di token del corpus...")
    # riduco la lista di liste ad una singola lista con tutto mergiato per poter contare le occorrenze dei termini
    all_list = chain.from_iterable(alltokens)
    term_freqs_all = Counter(all_list)

    print("Riduzione ad un'unica lista terminata.")

    for x in term_freqs_all.keys():
        storage.insert_terms_frequency(x, term_freqs_all[x])
    return

#save_frequency_allcorpus()