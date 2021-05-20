""" DB MANAGER """

from webapp.models import Product, Nutriment, Save


def add_data(data_list):

    is_exist = Product.objects.filter(code__iregex=f"{data_list[5]}")
    if len(is_exist) == 0:

        Product.objects.create(
            product_name=data_list[0],
            product_url=data_list[1],
            product_img=data_list[2],
            category=data_list[3],
            nutriscore=data_list[4],
            code=data_list[5],
            )


def add_nutr_data(nutr_data_list):

    is_exist = Nutriment.objects.filter(code__iregex=f"{nutr_data_list[0]}")
    if len(is_exist) == 0:
        Nutriment.objects.create(
            code=nutr_data_list[0],
            energy_100g=nutr_data_list[1],
            energy_unit=nutr_data_list[2],
            proteins_100g=nutr_data_list[3],
            fat_100g=nutr_data_list[4],
            saturated_fat_100g=nutr_data_list[5],
            carbohydrates_100g=nutr_data_list[6],
            sugars_100g=nutr_data_list[7],
            fiber_100g=nutr_data_list[8],
            salt_100g=nutr_data_list[9],
        )


def save_research(save_list):

    get_allready_registred = Save.objects.filter(
        user__iregex=f"{save_list[2]}"
        )

    for row in get_allready_registred:
        sub = row.substitute
        prod = row.product_substitued
        if prod == save_list[1]:
            if sub == save_list[0]:
                return

    Save.objects.create(
        user=save_list[2],
        substitute=save_list[0],
        product_substitued=save_list[1],
    )
