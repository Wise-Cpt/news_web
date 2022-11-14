from django.urls import path 
from .views import ArticleListView

app_name = 'core'

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='articleslist'),
]