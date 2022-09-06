from django.shortcuts import render
from django.views import View
from privod.models import *

class Home(View):
    def get(self, request):
        data = Product.objects.all()
        print(data)
        return render(request, 'index.html', {'data':data})

