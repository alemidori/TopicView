from gensim import corpora, models
import storage

dictionary = {}


def calculate_topic_distribution():

    corpus,dictionary = create_dictionary()
    # salvo una lista di array dove ogni array è un documento e
    # le coppie presenti nell'array sono rispettivamente (id_token, frequenza)

    # classe che prende un corpus il dizionario e il numero di topic (prende anche un parametro opzionale "iteration"
    # che se aumentato serve a migliorare il risultato)

    Lda_model = models.LdaModel(corpus, id2word=dictionary, num_topics=100)

    corpus_Lda = Lda_model[corpus]
    #corpora.BleiCorpus.serialize("tmp/corpus_stories.lda-c",corpus)
    corpora.BleiCorpus.serialize('tmp/corpus_stories.lda-c', corpus_Lda)

    return

def create_dictionary():

    stemmed = storage.get_stemmed_terms_paragraph()
    dictionary = corpora.Dictionary(stemmed)
    corpus = [dictionary.doc2bow(token) for token in stemmed]
    # salvo il dizionario in una specifica cartella così da utilizzarlo eventualmente in futuro
    # dictionary.save('tmp/dictionary.dict')
    print("Dizionario creato.")
    return corpus,dictionary

def load_lda_corpus():

    corpus_Lda = corpora.BleiCorpus("tmp/corpus_stories.lda-c")
    # stampa una serie di array aventi 100 coppie corrispondenti in questo caso ai 100 topic (se un topic non è per
    # niente presente in un documento la coppia non verrà mostrata affatto)
    # (se ci fossero tot topic stamperebbe tot coppie, ma solo se effettivamente nei documenti sono presenti)
    # in ciascuna delle coppie: (id_topic, distribuzione del documento su quel topic quindi più alto è il valore
    # e più il documento parlerà di quel tipic)
    for doc in corpus_Lda[:10]:
        print(doc)

    return