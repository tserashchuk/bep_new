from django.shortcuts import render
from django.views import View
from privod.models import *

class Home(View):
    def get(self, request):
        products = Product.objects.all()
        categorys = Category.objects.all()
        return render(request, 'index.html', {'products':products,'categorys':categorys})

