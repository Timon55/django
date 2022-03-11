from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsList.as_view(), name='home'),
    path('category/<int:category_id>/', NewsCategoryList.as_view(), name='category'),
    path('view_news/<int:news_id>/', ViewNews.as_view(), name='view_news'),
    path('add_news/', CreateNews.as_view(), name='add_news'),
]
