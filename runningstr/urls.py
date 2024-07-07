from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', video_view, name='video_view'),
]