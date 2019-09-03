from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Category, Note
from .form import CategoryForm, NoteForm
from django.urls import reverse_lazy
# Create your views here.


class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('notes:category-list')


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Category.objects.all()
        return context


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm

    def get_initial(self):
        initial = super().get_initial()
        initial['category'] = self.kwargs['pk']
        return initial

