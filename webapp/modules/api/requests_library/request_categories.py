""" GET SOME CATEGORIES """
import requests


def query_categories(number):

    list_of_categories = list()

    # TRUNCATE URI
    url = 'https://fr.openfoodfacts.org/categories.json'

    while len(list_of_categories) != number:

        categories_json = requests.get(url).json()

        for tag in categories_json["tags"]:
            category = tag.get("name", None)
            list_of_categories.append(category)

            if len(list_of_categories) == number:
                return list_of_categories

        return None
