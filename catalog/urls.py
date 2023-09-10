from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductDetailViews, ProductCreateView, ContactsCreateView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductCreateView.as_view(), name='home'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('<int:pk>/product/', ProductDetailViews.as_view(), name='view')
    # path('create/', ProductCreateView.as_view(), name='create')
]