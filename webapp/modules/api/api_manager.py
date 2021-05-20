"""
API RESEARCH
OPENFOODFACT

PEP8 exeptions: (flake8) E501 - line (9,10) too long * 2
"""

from webapp.modules.api.requests_library.request_categ import query_products
from webapp.modules.api.requests_library.request_categories import (
    query_categories
)
from webapp.modules.api.requests_library.request_products import (
    query_n_products
)
from webapp.modules.api.requests_library.request_code import by_code

from webapp.modules.tools.display import display_loading, display_start
from webapp.management.commands.config import nb_categories


def get_products(target, number, params, data):

    """ TO FILL PRODUCTS IN DB """
    if target == 'products':

        """ ALL PRODUCTS """
        if params == 'all' or params == "product_name":

            if params == 'all':
                """ GET WORK DATAS """
                categories = query_categories(nb_categories)
                """ INITIALYZE STATE """
                state = 0
                display_start()
                """ FOR EACH CATEGORIE IN LIST """
                for categorie in categories:
                    """ GET PRODUCTS """
                    query_products(
                        categorie,
                        int(number/nb_categories),
                        "to_fill"
                        )
                    state += (number/nb_categories)
                    display_loading(state, number)

            if params == 'product_name':
                products = query_n_products(data, number)
                return products

        elif params == 'by_code':
            product_data = by_code(data, 'result')
            return product_data

        elif params == 'nutriscore':
            products = query_products(data[0], number, ["substitute", data[1]])
            return products
