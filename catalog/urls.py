from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductDetailViews, ProductCreateView, ContactsCreateView, ProductListView, VersionListView, \
    VersionCreateView, toggle_activity

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailViews.as_view(), name='view'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('view_version/<int:pk>/', VersionListView.as_view(), name='view_version'),
    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
    # path('activity/<int:product_pk>/<int:version_pk>/', toggle_activity, name='toggle_activity'),
]