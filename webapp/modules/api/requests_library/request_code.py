"""
RESPONSE TO GIVEN CODE
"""
import requests


def by_code(code, params):

    """ BUILD URL """
    url_begin = 'http://world.openfoodfacts.org/api/v0/product/'
    url_end = '.json'

    url = f"{url_begin}{code}{url_end}"

    """ REQUEST """
    data = requests.get(url).json()

    if params == 'selection':
        return data
    elif params == 'result':
        prod = {}

        """ PRODUCTS DATA """

        prod["product_name"] = (
            data["product"].get("product_name_fr", None)
        )
        prod["product_url"] = (
            f"http://world.openfoodfacts.org/product/{code}"
        )

        try:
            prod["product_img"] = (
                data["product"]["selected_images"]["front"]["display"]["fr"]
            )
        except KeyError:
            prod["product_img"] = (
                data["product"].get("image_front_url", None)
            )

        prod["category"] = (
            data["product"].get("categories", None)
        )
        prod["nutriscore"] = (
            data["product"].get("nutriscore_grade", None)
        )
        prod["code"] = (
            data.get("code", None)
        )

        """ NUTRIMENTS """

        prod["energy_100g"] = (
            data["product"]["nutriments"].get("energy_100g", None)
        )
        prod["energy_unit"] = (
            data["product"]["nutriments"].get("energy_unit", None)
        )
        prod["proteins_100g"] = (
            data["product"]["nutriments"].get("proteins_100g", None)
        )
        prod["fat_100g"] = (
            data["product"]["nutriments"].get("fat_100g", None)
        )
        prod["saturated_fat_100g"] = (
            data["product"]["nutriments"].get("saturated-fat_100g", None)
        )
        prod["carbohydrates_100g"] = (
            data["product"]["nutriments"].get("carbohydrates_100g", None)
        )
        prod["sugars_100g"] = (
            data["product"]["nutriments"].get("sugars_100g", None)
        )
        prod["fiber_100g"] = (
            data["product"]["nutriments"].get("fiber_100g", 0)
        )
        prod["salt_100g"] = (
            data["product"]["nutriments"].get("salt_100g", None)
        )

        """ CLEAN CATEGORY """

        for pr in prod["category"].split(","):
            if pr.startswith("fr:"):
                prod["category"] = pr.replace("fr:", "")
        else:
            try:
                prod["category"] = prod["category"].split(",")[-2]
            except IndexError:
                prod["category"] = prod["category"].split(",")[0]

            if prod["category"].startswith("en:"):
                prod["category"].replace("en:", "")

        return prod
