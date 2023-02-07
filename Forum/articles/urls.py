from django.urls import path
from .views import ArticlesList, ArticleDetail, ArticleCreate, ArticleEdit, ArticleDelete

urlpatterns = [
    path('', ArticlesList.as_view(), name='articles_list'),
    path('<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete')
]