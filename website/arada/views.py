from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def home(request):
    info = ShopInformation.objects.all().first
    data={'info': info}
    return render(request, 'index.html',data)

def product(request):
    product = Product.objects.all()
    data={'product': product}
    return render(request,'product.html',data)
    


def contact(request):
    return render(request,'contactus.html')

