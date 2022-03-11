from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewsForm
from .models import News, Category
from django.views.generic import ListView, DetailView, CreateView

# класс конструктор
class NewsList(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'index.html'
    paginate_by = 3

    # переопределение родительской функции для фильтрации записей
    def get_queryset(self):
       return News.objects.filter(is_published=True).select_related('category')


class NewsCategoryList(ListView):
    model = Category
    context_object_name = 'news'
    template_name = 'category.html'
    allow_empty = False
    paginate_by = 3
    # переопределение родительской функции для фильтрации записей
    def get_queryset(self):
       return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'
    template_name = 'news/view_news.html'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'



