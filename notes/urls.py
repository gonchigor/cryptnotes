from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, NoteCreateView

app_name = 'notes'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('category/create', CategoryCreateView.as_view(), name='category-create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/create', NoteCreateView.as_view(), name='note-create')
]
