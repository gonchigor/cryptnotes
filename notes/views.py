from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, Note
# Create your views here.


class CategoryListView(ListView):
    model = Category
