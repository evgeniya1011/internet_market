import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        with open("data.json", "r", encoding="utf-8") as file:
            data = file.read()
            data_json = json.loads(data)
            products_for_create = []
            category_for_create = []
            for item in data_json:
                if item["model"] == "catalog.category":
                    category_for_create.append(Category(pk=item["pk"], **item["fields"]))
            Category.objects.bulk_create(category_for_create)
            for item in data_json:
                if item["model"] == "catalog.product":
                    product_name = item["fields"]["product_name"]
                    descriptions = item["fields"]["descriptions"]
                    picture = item["fields"]["picture"]
                    category = item["fields"]["category"]
                    category_inst = Category.objects.get(pk=category)
                    price = item["fields"]["price"]
                    date_create = item["fields"]["date_create"]
                    date_update = item["fields"]["date_update"]
                    products_for_create.append(Product(
                                pk=item["pk"],
                                product_name=product_name,
                                descriptions=descriptions,
                                picture=picture,
                                category=category_inst,
                                price=price,
                                date_create=date_create,
                                date_update=date_update
                    ))
            Product.objects.bulk_create(products_for_create)



