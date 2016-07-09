import evaluation

def main():
    place_categ,total_dict = evaluation.stem_categories_and_terms()
    evaluation.matching_categ(place_categ,total_dict)

    return

main()
