""" TO ANALIZE IF CODE IS IN OpenFF DB """

from webapp.models import Product
from webapp.modules.tools.display import display_analyze, display_delete

import requests


def update_db():

    code_list = Product.objects.values_list("code", flat=True)
    del_codes = []
    row = 1

    for code in code_list:

        """ BUILD URL """
        url_begin = 'http://world.openfoodfacts.org/api/v0/product/'
        url_end = '.json'

        url = f"{url_begin}{code}{url_end}"

        """ REQUEST """
        exist = requests.get(url).json()

        """ CHECK """
        if exist["status"] == 0:
            del_codes.append(code)

        """ DISPLAY ADVENCEMENT """
        display_analyze(row, code_list)
        row += 1

    """ DELETE PRODUCT WITH WRONG CODE """
    if len(del_codes) != 0:
        for code in del_codes:
            Product.objects.filter(code__iregex=fr"^{code}").delete()

            """ DISPLAY ADVENCEMENT """
            display_delete(row, del_codes)
    else:
        print("\n>>>    Aucune modification")
