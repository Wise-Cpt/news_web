from django.urls import path 
from django.conf.urls.static import static
from config import settings
from .views import ArticleListView, ArticleDetailView

app_name = 'core'

urlpatterns = [
    path('', ArticleListView.as_view(), name='articleslist'),
    path('article-<int:pk>', ArticleDetailView.as_view(), name='articledetail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
