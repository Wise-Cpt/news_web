from django.urls import path 
from django.conf.urls.static import static
from config import settings
from .views import ArticleListView, ArticleDetailView, ArticleList2View, Article2DetailView

app_name = 'core'

urlpatterns = [
    path('', ArticleListView.as_view(), name='articleslist'),
    path('article-liste_2', ArticleList2View.as_view(), name='articlelist2'),
    path('article-<int:pk>', ArticleDetailView.as_view(), name='articledetail'),
    path('article-liste_2/article-<int:pk>', Article2DetailView.as_view(), name='article2detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)