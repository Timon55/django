from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .models import News, Category
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import logout, login


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')

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



