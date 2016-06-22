import storage
import specificity
import show_html
from collections import Counter
import main_show_topic_distribution

def calculate_specific_terms(listmaintopic):

    main_show_topic_distribution.main()
    stories = []

    # for k in storage.paragraphs_coll.distinct('id_story'):
    #     stories.append(k)

    for k in storage.paragraphs_coll.distinct('id_story'):
        stories.append(k)

    increment_for_topiclist = 0

    for p in stories:
        print("Documento "+str(stories.index(p)))

        for k in storage.paragraphs_coll.find({'id_story': p},{'_id':0,'tokens':1, 'descr':1}):
            # strings.append(k['descr'])
            # paragtokens.append(k['tokens'])

        #for text in strings:
            #tokenlist = paragtokens[strings.index(text)]
            listwords = []
            for v in storage.topics_terms.find({'id_topic':listmaintopic[increment_for_topiclist]}, {'_id':0,'words_list':1}):
                listwords = v['words_list'] #lista prime 50 parole del topic date dall'LDA
            #print("Stampo le prime 5 parole specifiche...")

            finallist = specificity.get_specific_words(listmaintopic[increment_for_topiclist],listwords, k['tokens'])

            #specific_words_toshow = []
            # if len(specific_words) > 5:
            #     for n in range(0,5):
            #         specific_words_toshow.append(specific_words[n])
            # else:
            #     specific_words_toshow = specific_words

            show_html.fill_tables(p, k['descr'], listmaintopic[increment_for_topiclist], finallist)

            increment_for_topiclist += 1

        final_topic_dict = specificity.get_topic_dict()

        show_html.add_docrow_in_topic_description(stories.index(p))

        for key in final_topic_dict.keys():

            storage.save_topic_terms_union(key,final_topic_dict[key])
            show_html.fill_topicfile(key, dict(Counter(sum(final_topic_dict[key], []))))

        specificity.empty_topic_dict()
        print("Topic aggiunti nell'html")

    return
