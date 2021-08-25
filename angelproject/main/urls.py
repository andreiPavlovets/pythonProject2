from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('blog', blog),
    path('courses', courses),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail')
]