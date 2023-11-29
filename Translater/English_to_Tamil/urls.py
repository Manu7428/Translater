from django.urls import path
from . import views

urlpatterns = [
    path('find/', views.translater,name="path")
]