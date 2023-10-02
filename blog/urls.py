from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name
urlpatterns = [
    path('create/', never_cache(ArticleCreateView.as_view()), name='create'),
    path('', ArticleListView.as_view(), name='list'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete')
]