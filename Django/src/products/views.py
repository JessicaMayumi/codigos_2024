from django.shortcuts import render

from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=3)
    context = {
        "title": obj.title,
        "description": obj.description
    }
    return render(request, "products/products_details.html", context)

'''def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, "products/products_create.html", context)'''

def product_create_view(request):
    my_form = RawProductForm(request.POST or None)
    context = {
        "form" : my_form
    }
    return render(request, "products/products_create.html", context)