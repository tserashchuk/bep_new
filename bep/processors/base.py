from privod.models import Category, Manufacturer
from django.db.models.functions import Length

def category_processor(request):
    categorys=Category.objects.all().order_by(Length('cat_name').asc())
    manufacturers = Manufacturer.objects.all().order_by(Length('manufacturer_name').asc())
    data = [categorys[i:i+3] for i in range(0, len(categorys), 3)]
    data_manufacturer = [manufacturers[i:i+3] for i in range(0, len(manufacturers), 3)]
    return ({'catprocessor':categorys, 'manufacturers':manufacturers, 'data':data, 'data_manufacturer':data_manufacturer})