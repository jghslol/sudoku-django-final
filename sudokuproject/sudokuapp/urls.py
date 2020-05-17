from django.urls import path
from sudokuapp.views import index

urlpatterns = [
    path('', views.index, name='index'),


]
