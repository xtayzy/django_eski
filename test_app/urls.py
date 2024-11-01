from django.urls import path
from test_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
