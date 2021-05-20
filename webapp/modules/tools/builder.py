"""
BUILDER FILE
to build response for HTML ressources
"""

from webapp.models import Product
from webapp.modules.api.api_manager import get_products

list_of_nutr = ["a", "b", "c", "d", "e"]


def build_data(data, target):
    datas = {}
    list_selection = []
    response = list()
    products = list()
    prod = 0

    """ FOR PRODUCT PAGE """
    if target == "code":
        products = Product.objects.filter(code__exact=f"{data}")
        if len(products) == 0:
            response = get_products("products", 1, "by_code", data)

    """ FOR SELECTION """
    if target == "prod_name":
        check_list = 0

        products = Product.objects.filter(product_name__iregex=fr"^{data}")

        for row in products:
            check_list += 1

        """ NEED 6 PRODUCTS """
        if check_list < 6:
            products = None

            response = get_products("products", 6, "product_name", data)
            if response is not None:
                if len(response) < 6:
                    check_list = None

    """ FOR RESULTS """
    if target == "substitute":
        c_categ = data[0]
        c_nutr = data[1]
        is_response = False
        for nutr in list_of_nutr:
            """ IF NUTRISCORE IS > TO TARGET NUTRISCORE """
            products = Product.objects.filter(
                category__iregex=fr"^{c_categ}",
                nutriscore__exact=f"{nutr}").order_by('nutriscore')

            """ COUNT OF SUBSTITUTES """
            check_list = 0

            for row in products:
                check_list += 1

            """ IF ITS NOT ENOUGHT, CREATE IT """
            if check_list < 6:
                if list_of_nutr.index(nutr) < list_of_nutr.index(c_nutr):
                    products = None
                    """ GET IT FROM API """
                    data_product = [c_categ, c_nutr]
                    response = get_products(
                        "products",
                        6,
                        "nutriscore",
                        data_product
                        )
                    if response:
                        if len(response) == 6:
                            products = None
                            is_response = True
                            break
                    if is_response:
                        break
                else:
                    products = None
                    is_response = True
            elif check_list >= 6:
                response = None
                is_response = True
                break

    """ BUILD RESPONSE """
    while prod < 7:
        """ IF PRODUCTS IN DB """
        if products and not response:
            """ FOR EACH PRODUCT """
            for row in products:
                dict_prod = {}
                dict_prod["product_name"] = row.product_name
                dict_prod["category"] = row.category
                dict_prod["product_img"] = row.product_img
                dict_prod["nutriscore"] = row.nutriscore
                dict_prod["product_url"] = row.product_url
                dict_prod["code"] = row.code

                list_selection.append(dict_prod)

                prod += 1

                if target == "code":
                    """ RESEARCH BY CODE COMPLETED """
                    datas["products"] = list_selection
                    return datas

        elif response and not products:
            if target == "prod_name" or target == "substitute":
                for row in response:
                    dict_prod = {}
                    dict_prod["product_name"] = response[row][0][0]
                    dict_prod["product_url"] = response[row][0][1]
                    dict_prod["product_img"] = response[row][0][2]
                    dict_prod["category"] = response[row][0][3]
                    dict_prod["nutriscore"] = response[row][0][4]
                    dict_prod["code"] = response[row][0][5]

                    list_selection.append(dict_prod)

                    prod += 1

            elif target == "code":
                """ RESEARCH BY CODE COMPLETED """
                list_selection.append(response)
                datas["products"] = list_selection
                return datas

        elif len(list_selection) <= 0:
            return

        if prod >= 6:
            if target == "prod_name":
                datas["products"] = list_selection
                return datas
            if target == "substitute":
                return list_selection[0:6]
