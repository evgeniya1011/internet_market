from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'preview', 'is_published', 'view_count')
    success_url = reverse_lazy('blog:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Создайте статью, заполнив следующие данные:"
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()

        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        if self.object.view_count == 100:
            send_mail('Просмотры', 'Поздравляем!Вы набрали 100 просмотров', 'zhdavydova@mail.ru', ['avards222@yandex.ru'])
        return self.object

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'slug', 'body', 'preview', 'is_published', 'view_count')
    success_url = reverse_lazy('blog:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Отредактируйте статью:"
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:list')










