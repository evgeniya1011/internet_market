from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductDetailViews, ProductCreateView, ContactsCreateView, ProductUpdateWithVersionView, ProductCategoryListView, CategoryListView

app_name = CatalogConfig.name
urlpatterns = [
    path('', CategoryListView.as_view(), name='list'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailViews.as_view()), name='view'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create'),
    path('edit/<int:pk>', ProductUpdateWithVersionView.as_view(), name='edit'),
    path('catalog/<int:pk>', ProductCategoryListView.as_view(), name='view_product')
]