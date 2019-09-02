from django.urls import path
from .views import CategoryListView, CategoryCreateView

app_name = 'notes'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('category/create', CategoryCreateView.as_view(), name='category-create'),
]
