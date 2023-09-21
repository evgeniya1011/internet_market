from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, ListView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, Category, Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductListView(ListView):
    model = Product
    content_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.order_by('-date_create')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Наши товары'
        return context_data


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self, *args, **kwargs):
        product_pk = self.object.product.pk
        return reverse('catalog:view_version', kwargs={'pk': product_pk})


class VersionListView(ListView):
    model = Version

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(product=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['version_pk'] = product_item.pk
        context_data['title'] = f"Версии товара {product_item.product_name.title()}"
        return context_data


# def toggle_activity(request, product_pk, version_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#     version_item = get_object_or_404(Version, pk=version_pk, product=product)
#     if version_item.is_active:
#         version_item.is_active = False
#     else:
#         version_item.is_active = True
#     version_item.save()
#     return redirect(reverse('catalog:view_version', args=[product_pk]))


def toggle_activity(request, pk):
    product = get_object_or_404(Product, pk=pk)
    version_item = get_object_or_404(Version, product=product)

    if version_item.is_active:
        version_item.is_active = False
    else:
        version_item.is_active = True
    version_item.save()
    return redirect(reverse('catalog:view_version', args=[pk]))


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


class ProductDetailViews(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product_name = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['object'] = product_name
        return context_data
