""" DISPLAY FILE """
import sys


def display_start():
    print("\n>>>    Recherche et ajout d'aliments dans la base de données")


def display_loading(state, target):

    """ PRINT THE PRODUCT LOADING """
    loading = (state*100/target)
    sys.stdout.write(
            f"\r>>>    Remplissage: {int(loading)}%"
    )


def display_analyze(row, code_list):
    percent = round(row / len(code_list) * 100, 2)
    sys.stdout.write(
                    f"\r>>>    Vérification {percent}%"
                    )


def display_delete(row, del_codes):
    percent = round(row / len(del_codes) * 100, 2)
    sys.stdout.write(
                    f"\r>>>    Suppression {percent}%"
                    )
