""" CONFIG TO CONNECT DB """

import psycopg2
import os

""" POSTGRE SETTINGS """
settings = os.environ.get("Psql_purbeurre").split()

conn = psycopg2.connect(
    user=settings[0],
    password=settings[1],
    host=settings[2],
    port="",
    database=settings[3]
)

cur = conn.cursor()

""" CONSTANTS SETTING """
nb_categories = 50
nb_of_products = 500
