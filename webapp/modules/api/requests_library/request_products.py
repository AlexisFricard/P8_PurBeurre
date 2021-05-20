"""
REQUEST PRODUCTS BY NAME
"""
import requests

import webapp.modules.api.analysis.analysis_data as ad
analysis = ad.Analyze_data()


def query_n_products(data, number):

    nb_of_products = 0
    page = 1
    products_dict = {}
    list_of_code = list()

    """ WHILE LOOP """
    while page < 10:

        """ BUILD URL """
        url_begin = 'https://fr.openfoodfacts.org/cgi/search.pl?search_terms='
        url_end = '&search_simple=1&action=process&json=1'
        url_page = f'&page={page}'

        url = f"{url_begin}{data}{url_end}{url_page}"

        """ REQUEST """
        data_prod = requests.get(url).json()
        """ MAIN LOOP """
        for prod in data_prod["products"]:
            check_data = True
            """ TRY/EXCEPT TO PASS KEY ERROR """
            try:
                product_name = prod.get("product_name_fr", None)
                product_url = prod.get("url", None)
                product_img = (
                    prod["selected_images"]["front"]["display"].get("fr", None)
                )
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

                data_nutr = [code, energy_100g, energy_unit,
                             proteins_100g, fat_100g,
                             saturated_fat_100g, carbohydrates_100g,
                             sugars_100g, fiber_100g, salt_100g]
                """ CLEAN CATEGORY """
                if category:
                    try:
                        category = category.split(",")[-2]
                    except IndexError:
                        category = category.split(",")[0]

                data = (product_name, product_url, product_img,
                        category, nutriscore, code)

                """ CHECK PRODUCT DATAS """
                for d in data:
                    if not analysis.checking_empty_field(d):
                        check_data = False

                for d in data_nutr:
                    if not analysis.checking_empty_field(d):
                        check_data = False

                """ IF ITS VALID DATA """
                if check_data is True:
                    """ IF NOT ALLREADY GET / by_code"""
                    if code not in list_of_code:
                        list_of_code.append(code)

                        nb_of_products += 1

                        products_dict[product_name] = [data, data_nutr]

                        if len(products_dict) >= number:
                            return products_dict

            except KeyError as error:
                print(KeyError, error)
                pass

        page += 1
