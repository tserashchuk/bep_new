from privod.models import Category

def category_processor(request):
    categorys=Category.objects.all()
    catcount = categorys.count
    
    return ({'catprocessor':categorys,'catcount':catcount})