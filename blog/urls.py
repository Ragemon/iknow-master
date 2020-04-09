from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
        path('', views.ArticleListView.as_view(), name='article_list'),
        path('<int:pk>/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
        path('', views.post_update, name='update'),
        path('', views.post_delete, name='delete'),
        path('', views.post_delete, name='detail'),

]
