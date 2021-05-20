"""
Test DB_Manager
"""

from webapp.modules.psql.db_manager import (add_data, add_nutr_data,
                                            save_research)
from webapp.models import Product, Nutriment, Save


def test_save_research():

    # VARS
    list = ['codeOfSubstitute', 'codeOfProduct', 'johndoe']

    # EXECUTE FUNCTION
    save_research(list)

    """ TEST - IF WAS ADDED AND DELETE IT """
    assert Save.objects.get(user='johndoe').delete()


def test_add_data():

    # VARS
    list = ['NameOfProduct', 'UrlOfProduct', 'UrlImgOfProduct',
            'CategorieOfProduct', 'Nutr', 'CodeOfProduct']

    # EXECUTE FUNCTION
    add_data(list)

    """ TEST - IF WAS ADDED AND DELETE IT """
    assert Product.objects.get(product_name='NameOfProduct').delete()


def test_add_nutr_data():

    # VARS
    list = ['CodeOfProduct', 0, 'unit', 0, 0, 0, 0, 0, 0, 0]

    # EXECUTE FUNCTION
    add_nutr_data(list)

    """ TEST - IF WAS ADDED AND DELETE IT """
    assert Nutriment.objects.get(code='CodeOfProduct').delete()
