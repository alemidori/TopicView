'''si occupa del salvataggio dei testi in un file json accessibile mediante mongodb e dell'accesso
a questi utlimi'''

import pymongo
import json

client = pymongo.MongoClient()
db = client['stories']

paragraphs_coll = db['paragraphs']
terms_ref_coll = db['terms_ref']

#prende 3 parametri: l'id del racconto originale nel quale il paragrafo si trova
#il testo del paragrafo e la posizione all'interno del racconto

def insert_paragraph(story_id, text, position, list_of_tokens):
    paragraphs_coll.insert_one({'id_story': story_id, 'descr': text, 'pos': position, 'tokens': list_of_tokens})
    return

def insert_terms_ref(dict):
    for k,v in dict.items():
        json_toExport = {'token' : k, 'originals' : v}
        terms_ref_coll.insert_one(json_toExport)
    return

#prende per ogni paragrafo nella collezione la lista dei token associati
def get_stemmed_terms_paragraph():

    token_list_paragraph = []
    cursor = paragraphs_coll.find(None, {"tokens": 1, '_id': 0})  # metto None perche' sto facendo una selezione su niente quindi voglio che mi restituisca tutto
    for element in cursor:
        token_list_paragraph.append(element['tokens'])  #e' una lista di liste in cui ogni lista interna ha i token
        # riferiti ad ogni singolo paragrafo
    return token_list_paragraph

def get_paragr_descr_from_id(idstory, pos):
    cursor = paragraphs_coll.find({'id_story': idstory,'pos':pos}, {'_id': 0, 'descr': 1})
    a = ""
    for element in cursor:
        a = element['descr']
    return a

