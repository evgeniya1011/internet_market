from django.contrib import admin

from catalog.models import Product, Category, Contacts


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'descriptions',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'ph_number', 'message',)