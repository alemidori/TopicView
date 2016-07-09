import storage
import processing
import topic_specific_terms



def stem_categories_and_terms():

    places = []
    place_stemmed_categ_dict = {}

    for n in storage.business_terms_coll.find(None, {'place': 1, '_id': 0}):
        places.append(n['place'])

    for p in places:
        for place in storage.business_coll.find({'business_id': p}, {'categories': 1, 'business_id': 1, '_id': 0}):
            stemmed_categ = []
            for categ in place['categories']:
                if "&" in str(categ):
                    spl = str(categ).split("&")
                    for n in range(0, len(spl)):
                        stemmed_categ.append(spl[n])
                else:
                    stemmed_categ.append(processing.process_string(str(categ)))

            place_stemmed_categ_dict[place['business_id']] = [stemmed_categ]


    #-------------------------------------------------------------------------

    total_terms_dict = {}
    for k in storage.business_terms_coll.find(None, {'place': 1, 'terms_list': 1, '_id': 0}):
        total_terms_dict[k['place']] = [processing.process_string(n) for n in sum(k['terms_list'],[])]


    return place_stemmed_categ_dict,total_terms_dict



def matching_categ(place_dict,total_dict):


    for key in place_dict.keys():
        incr = 0
        for list_categ in place_dict[key]:
            for elem in list_categ:
                if elem in total_dict[key]:
                    incr += 1
        print("Locale con ID: "+str(key))
        print(str(incr)+" categorie presenti su "+str(len(total_dict[key]))+" termini totali.")
        print("Percenuale: "+ str(float(incr)/float(len(total_dict[key]))))

    return
