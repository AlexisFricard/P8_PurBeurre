"""
REQUEST BY CATEG

PEP8 exeptions: (flake8) E501 - line too long * 4
"""
import requests

import webapp.modules.api.analysis.analysis_data as ad
from webapp.modules.psql.db_manager import add_data, add_nutr_data

analysis = ad.Analyze_data()
list_of_nutr = ["a", "b", "c", "d", "e"]


def query_products(category, number, params):

    products_dict = {}
    nb_of_products = 0
    list_of_code = list()

    if params == "to_fill":
        client_nutr = ""
    elif params[0] == "substitute":
        client_nutr = params[1]
        params = "substitute"
    else:
        return None

    nb_page = 1

    while nb_page < 10:

        # BUILD URL FOR REQUEST
        url_begin = "https://fr.openfoodfacts.org/categorie/"
        parameter = f"{category}/{nb_page}"
        url_end = "&json=1&sort_by=nutriscore_score"
        url = f"{url_begin}{parameter}{url_end}"

        """ REQUEST """
        data_prod = requests.get(url).json()

        """ MAIN LOOP """
        for prod in data_prod["products"]:
            check_data = True
            """ TRY/EXCEPT TO PASS KEY ERROR """
            try:
                product_name = prod.get("product_name_fr", None)
                product_url = prod.get("url", None)

                try:
                    product_img = (
                        prod["selected_images"]["front"]["display"]["fr"]
                    )
                except KeyError:
                    product_img = prod.get("image_front_url", None)

                category = prod.get("categories", None)
                nutriscore = prod.get("nutriscore_grade", None)
                code = prod.get("code", None)

                energy_100g = prod["nutriments"].get("energy_100g", None)
                energy_unit = prod["nutriments"].get("energy_unit", None)
                proteins_100g = prod["nutriments"].get("proteins_100g", None)
                fat_100g = prod["nutriments"].get("fat_100g", None)
                saturated_fat_100g = (
                    prod["nutriments"].get("saturated-fat_100g", None)
                )
                carbohydrates_100g = (
                    prod["nutriments"].get("carbohydrates_100g", None)
                )
                sugars_100g = prod["nutriments"].get("sugars_100g", None)
                fiber_100g = prod["nutriments"].get("fiber_100g", 0)
                salt_100g = prod["nutriments"].get("salt_100g", None)

                data_nutr = [code, energy_100g, energy_unit, proteins_100g,
                             fat_100g, saturated_fat_100g, carbohydrates_100g,
                             sugars_100g, fiber_100g, salt_100g]

                """ CLEAN CATEGORY """
                if category:
                    for pr in category.split(","):
                        if pr.startswith("fr:"):
                            category = pr.replace("fr:", "")
                    else:
                        try:
                            category = category.split(",")[-2]
                        except IndexError:
                            category = category.split(",")[0]
                        if category.startswith("en:"):
                            category.replace("en:", "")

                data = (product_name, product_url, product_img,
                        category, nutriscore, code)

                """ CHECK PRODUCT DATAS """
                for d in data:
                    if not analysis.checking_empty_field(d):
                        check_data = False

                for d in data_nutr:
                    if not analysis.checking_empty_field(d):
                        check_data = False

                if params == "substitute" and check_data is True:
                    score_nutr = list_of_nutr.index(nutriscore)
                    score_client_nutr = list_of_nutr.index(client_nutr)
                    if score_nutr >= score_client_nutr:
                        check_data = False

                """ IF ITS VALID DATA """
                if check_data is True:
                    """ IF NOT ALLREADY GET / by_code"""
                    if code not in list_of_code:
                        list_of_code.append(code)

                        if params == "to_fill":
                            add_data(data)
                            add_nutr_data(data_nutr)

                        nb_of_products += 1

                        products_dict[product_name] = [data, data_nutr]

                        if nb_of_products >= number:
                            return products_dict

            except KeyError as error:
                if params != "to_fill":
                    print(KeyError, error)

        nb_page += 1
