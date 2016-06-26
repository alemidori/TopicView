import storage
import specificity
import show_html
from collections import Counter
import main_show_topic_distribution
from operator import itemgetter

def calculate_specific_terms(listmaintopic):

    main_show_topic_distribution.main()
    stories = []

    for k in storage.paragraphs_coll.distinct('id_story'):
        stories.append(k)

    increment_for_topiclist = 0

    for p in stories:
        print("Documento "+str(stories.index(p)))

        finallist = []
        for k in storage.paragraphs_coll.find({'id_story': p},{'_id':0,'tokens':1}):
            listwords = []
            for v in storage.topics_terms.find({'id_topic':listmaintopic[increment_for_topiclist]}, {'_id':0,'words_list':1}):
                listwords = v['words_list'] #lista prime 50 parole del topic date dall'LDA

            finallist.append(specificity.get_specific_words(listmaintopic[increment_for_topiclist],listwords, k['tokens']))

            increment_for_topiclist += 1

        final_topic_dict = specificity.get_topic_dict()

        # print("Scrivo tabella nell'html...")
        #
        # increment_for_topiclist = 0
        # for k in storage.paragraphs_coll.find({'id_story': p}, {'_id': 0, 'descr': 1}):
        #     show_html.fill_tables(p, k['descr'], listmaintopic[increment_for_topiclist],
        #                           final_topic_dict[listmaintopic[increment_for_topiclist]],finallist[increment_for_topiclist])
        #     increment_for_topiclist += 1
        #
        # print("Tabella aggiunta nell'html")

        show_html.add_docrow_in_topic_description(stories.index(p))

        for key in final_topic_dict.keys():
            show_html.fill_topicfile(key, sorted(dict(Counter(sum(final_topic_dict[key], []))).items(),key=itemgetter(1),reverse=True))

        specificity.empty_topic_dict()
        print("Topic aggiunti nell'html")

    return
