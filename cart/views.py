from django.shortcuts import render
from product.models import Product
# Create your views here.
def item_list(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request,'products.html',context)