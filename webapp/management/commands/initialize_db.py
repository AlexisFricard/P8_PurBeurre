"""
COMMAND TO INITIALIZE DATA BASE
"""
from django.core.management.base import BaseCommand

from webapp.modules.api.api_manager import get_products
from webapp.management.commands.analyze_db import update_db
from webapp.management.commands.config import nb_of_products
from webapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not bool(Product.objects.all()):
            get_products("products", nb_of_products, "all", '')
        else:
            update_db()
