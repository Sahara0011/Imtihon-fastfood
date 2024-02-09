from django.shortcuts import render
from menu.models import Product, ProductType


# Create your views here.
def home_page(request):
    all_product_type = ProductType.objects.all()
    all_product = Product.objects.all()
    context = {
        "all_product_type": all_product_type,
        "all_product": all_product,
    }
    return render(request=request, template_name='index.html', context=context)
