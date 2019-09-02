from django.urls import path
from .views import CategoryListView

app_name = 'notes'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
]
