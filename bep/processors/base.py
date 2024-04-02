from privod.models import Category, Manufacturer, Producttag
from django.db.models.functions import Length

def category_processor(request):
    categorys=Category.objects.all().order_by(Length('cat_name').asc())
    manufacturers = Manufacturer.objects.all().order_by(Length('manufacturer_name').asc())
    producttags = Producttag.objects.all().order_by(Length('tag_name').asc())
    return ({'catprocessor_base':categorys, 'manufacturers_base':manufacturers, 'producttags_base':producttags})