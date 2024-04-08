from django.shortcuts import render
from django.views import View
from privod.models import *
from django.db.models.functions import Length
import json
from django.http import HttpResponse
class Home(View):
    def get(self, request):
        products = Product.objects.filter(pin_main=True)
        categorys = Category.objects.filter(pin_main_first=True).order_by(Length('cat_name'))
        categorys_sec = Category.objects.filter(pin_main_sec=True).order_by(Length('cat_name'))
        return render(request, 'index.html', {'products':products,'categorys':categorys,'categorys_sec':categorys_sec})

class Categorys(View):
    def get(self, request):
        categorys = Category.objects.all()
        return render(request, 'categorys.html', {'categorys':categorys})

class Products(View):
    def get(self, request, cat_slug):
        category = Category.objects.get(cat_slug=cat_slug)
        manufacturers = Manufacturer.objects.all()
        return render(request, 'products.html', {'category': category, 'manufacturers':manufacturers})
    
class ProductTags(View):
    def get(self, request, tag_slug):
        producttags = Producttag.objects.get(tag_slug=tag_slug)
        manufacturers = Manufacturer.objects.all()
        return render(request, 'tags.html', {'producttags': producttags, 'manufacturers':manufacturers})

class SingleProduct(View):
    def get(self, request, product_slug):
        product = Product.objects.get(product_slug=product_slug)
        return render(request, 'product.html', {'product': product})

class Contacts(View):
    def get(self, request):
        regions = Region.objects.all()
        return render(request, 'contact.html', {'regions':regions})
    
class Manufacturers(View):
    def get(self, request, manufacturer_slug):
        manufacturer = Manufacturer.objects.get(manufacturer_slug=manufacturer_slug)
        products_sliced = Product.objects.filter(manufacturer=manufacturer)[:6]
        products_man = Product.objects.filter(manufacturer=manufacturer)
        classes = ['d-sm-inline-block mt-n10','col-3 d-sm-inline-block  mt-lg-n8', 'd-lg-inline-block mt-n4','d-sm-inline-block  mt-n7', 'col-3 d-sm-inline-block  mt-lg-n10',' d-lg-inline-block']
        datas = zip(classes, products_sliced)
        return render(request, 'manufacturer.html', {'datas':datas,'manufacturer':manufacturer,'products_man':products_man})
    
class Search(View):

    def post(self, request):
        senddata = []
      
        data = json.loads(request.body)
        products = Product.objects.all()
    
        for product in products:
            if product.product_name.lower().find(str(data['searchquery']).lower()) != -1:
                senddata.append([product.product_name, product.product_slug])
        return HttpResponse(json.dumps(senddata), content_type="application/json")