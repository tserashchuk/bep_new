from privod.models import Category, Manufacturer, Producttag, Product
from django.db.models.functions import Length
import random

def category_processor(request):
    categorys=Category.objects.all().order_by(Length('cat_name').asc())
    manufacturers = Manufacturer.objects.all().order_by(Length('manufacturer_name').asc())
    producttags = Producttag.objects.all().order_by(Length('tag_name').asc())



    items = list(Product.objects.all())
    random_items = random.sample(items, 10)
    random_item = random.choice(items)

    return ({'catprocessor_base':categorys, 'manufacturers_base':manufacturers, 'producttags_base':producttags, 
             'random_item':random_items})