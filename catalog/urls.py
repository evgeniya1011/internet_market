from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductDetailViews, ProductCreateView, ContactsCreateView, ProductListView, ProductUpdateWithVersionView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailViews.as_view(), name='view'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>', ProductUpdateWithVersionView.as_view(), name='edit'),
]