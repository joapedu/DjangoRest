from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app.views import SkinList, SkinDetail

urlpatterns = [
    path('skin/', SkinList.as_view()),
    path('skin/<int:pk>/', SkinDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)