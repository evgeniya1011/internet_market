from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView

from catalog.forms import ProductForm, VersionBaseInlineFormSet, VersionForm
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


class ProductUpdateWithVersionView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:view', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1, formset=VersionBaseInlineFormSet)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        # self.object = form.save()
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()
                else:
                    return super().form_invalid(form)
        return super().form_valid(form)


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
