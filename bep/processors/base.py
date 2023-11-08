from privod.models import Category

def category_processor(request):
    categorys=Category.objects.all()
    catcount = categorys.count()//2
    first_menu_data = categorys[:catcount]
    second_menu_data = categorys[catcount:]
    
    return ({'catprocessor':categorys, 'catcount':catcount, 'first_menu_data':first_menu_data, 'second_menu_data':second_menu_data})