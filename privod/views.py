from django.shortcuts import render
from django.views import View
from privod.models import *

class Home(View):
    def get(self, request):
        products = Product.objects.filter(pin_main=True)
        categorys = Category.objects.filter(pin_main_first=True)
        categorys_sec = Category.objects.filter(pin_main_sec=True)
        return render(request, 'index.html', {'products':products,'categorys':categorys,'categorys_sec':categorys_sec})

class Categorys(View):
    def get(self, request):
        categorys = Category.objects.all()
        return render(request, 'categorys.html', {'categorys':categorys})

class Products(View):
    def get(self, request, cat_slug):
        category = Category.objects.get(cat_slug=cat_slug)
        return render(request, 'products.html', {'category': category})

class SingleProduct(View):
    def get(self, request, product_slug):
        product = Product.objects.get(product_slug=product_slug)
        return render(request, 'product.html', {'product': product})

class Contacts(View):
    def get(self, request):
        return render(request, 'contact.html')