"""
VIEWS FILE MANAGE PRODUCTS
"""
from django.shortcuts import render, redirect

from webapp.modules.tools.clean_sentence import remove_special_char
from webapp.modules.tools.builder import build_data
from webapp.modules.psql.db_manager import save_research
from webapp.modules.psql.db_manager import add_data, add_nutr_data


def index(request):
    return render(request, 'index.html')


def legal_notices(request):
    return render(request, 'legal_notices.html')


def selection(request):

    if request.method == "POST":
        query = request.POST.get('user_text')
        query_clnd = remove_special_char(query, "add_space")
        if query_clnd != "":
            datas = build_data(query_clnd, "prod_name")
            return render(request, 'selection.html', datas)
        else:
            return redirect('index')
    else:
        return redirect('index')


def result(request):

    if request.method == "GET":
        code = request.GET.get('query')

        """ GET CATEGORY AND NUTRISCORE FROM SELECTED PRODUCT """
        datas = build_data(code, "code")

        """ GET SUBSTITUTES """
        data_product = [
            datas["products"][0]["category"],
            datas["products"][0]["nutriscore"],
        ]
        datas["substitutes"] = build_data(data_product, "substitute")

        return render(request, 'results.html', datas)


def save(request):
    if request.method == "GET":
        data = request.GET.get('query')
        datas = data.replace(",", " ").split()

        if request.user.is_authenticated:
            for code in datas:
                products = build_data(code, "code")
                product = products["products"][0]
                try:
                    data_prod = [
                        product["product_name"],
                        product["product_url"],
                        product["product_img"],
                        product["category"],
                        product["nutriscore"],
                        product["code"],
                    ]
                    data_nutr = [
                        product["code"],
                        product["energy_100g"],
                        product["energy_unit"],
                        product["proteins_100g"],
                        product["fat_100g"],
                        product["saturated_fat_100g"],
                        product["carbohydrates_100g"],
                        product["sugars_100g"],
                        product["fiber_100g"],
                        product["salt_100g"],
                    ]

                    add_data(data_prod)
                    add_nutr_data(data_nutr)

                except KeyError as error:
                    print(KeyError, error)
                    pass

            datas.append(request.user.email)
            save_research(datas)
            return redirect('myfood')

        else:
            return redirect('signin')
