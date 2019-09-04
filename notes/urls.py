from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, NoteCreateView, \
    NoteDetailView, NoteDeleteView

app_name = 'notes'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('category/create', CategoryCreateView.as_view(), name='category-create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/create', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('note/<int:pk>/delete', NoteDeleteView.as_view(), name='note-delete'),
]
