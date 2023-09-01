from django.shortcuts import render
import json
from catalog.models import Product, Contacts


def home(request):
    last_products = Product.objects.order_by('-date_create')[:5]
    for product in last_products:
        print(product.product_name)
    return render(request, 'catalog/home.html')

def contacts(request):
    contact_list = []
    if request.method == "POST":
        name = request.POST.get("name")
        ph_number = request.POST.get("phone")
        message = request.POST.get("message")
        Contacts.objects.create(contact_name=name, ph_number=ph_number, message=message)
    return render(request, 'catalog/contacts.html')
