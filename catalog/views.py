from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView

from catalog.models import Product, Contacts, Category


# def home(request):
#     if request.method == "POST":
#         product_name = request.POST.get("name")
#         descriptions = request.POST.get("descriptions")
#         picture = request.POST.get("picture")
#         category = request.POST.get("category")
#         category_inst = Category.objects.get(pk=category)
#         price = request.POST.get("price")
#         date_create = request.POST.get("date_create")
#         date_update = request.POST.get("date_update")
#         Product.objects.create(product_name=product_name, descriptions=descriptions, picture=picture, category=category_inst, price=price, date_create=date_create, date_update=date_update)
#
#     last_products = Product.objects.order_by('-date_create')
#     for item in last_products[:5]:
#         print(item.product_name)
#
#     products = last_products.all()
#     paginator = Paginator(products, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'page_obj': page_obj,
#         'title': 'Наши товары'
#     }
#     return render(request, 'catalog/home.html', context)


class ProductCreateView(CreateView, ListView):
    model = Product
    template_name = "catalog/home.html"
    fields = ["product_name", "descriptions", "picture", "category", "price"]
    content_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.order_by('-date_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Наши товары'
        return context

    def post(self, request):
        product_name = request.POST.get("name")
        descriptions = request.POST.get("descriptions")
        picture = request.POST.get("picture")
        category = request.POST.get("category")
        category_inst = Category.objects.get(pk=category)
        price = request.POST.get("price")
        date_create = request.POST.get("date_create")
        date_update = request.POST.get("date_update")
        Product.objects.create(
            product_name=product_name,
            descriptions=descriptions,
            picture=picture,
            category=category_inst,
            price=price,
            date_create=date_create,
            date_update=date_update
        )
        return HttpResponseRedirect(self.request.path_info)


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         ph_number = request.POST.get("phone")
#         message = request.POST.get("message")
#         Contacts.objects.create(contact_name=name, ph_number=ph_number, message=message)
#     return render(request, 'catalog/contacts.html')

class ContactsCreateView(CreateView):
    model = Contacts
    template_name = "catalog/contacts.html"
    fields = ["contact_name", "ph_number", "message"]

    def post(self, request):
        contact_name = request.POST.get("name")
        ph_number = request.POST.get("phone")
        message = request.POST.get("message")
        Contacts.objects.create(
            contact_name=contact_name,
            ph_number=ph_number,
            message=message
        )
        return HttpResponseRedirect(self.request.path_info)



# def product(request, pk):
#     product_name = Product.objects.get(pk=pk)
#     context = {
#         'object': product_name
#     }
#     return render(request, 'catalog/product_detail.html', context)

class ProductDetailViews(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product_name = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['object'] = product_name
        return context_data
