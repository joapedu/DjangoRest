from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app.views import PostList, PostDetail, CategoriaList, CategoriaDetail

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('categories/', CategoriaList.as_view()),
    path('categories/<int:pk>/', CategoriaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)