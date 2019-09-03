from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Category, Note
from .form import CategoryForm, NoteForm, PasswordForm
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from .crypto import encrypt_message, password_hasher, password_verify, decrypt_message
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.text = encrypt_message(self.object.text, self.object.password)
        self.object.password = password_hasher(self.object.password)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('notes:category-detail', kwargs={'pk': self.kwargs['pk']})


class NoteDetailView(DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['object_list'] = Category.objects.all()
        context['form'] = PasswordForm()
        context['print'] = self.request.method == 'POST' and password_verify(self.request.POST['password'],
                                                                             self.object.password)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.method == 'POST' and password_verify(self.request.POST['password'], obj.password):
            obj.text = decrypt_message(obj.text, self.request.POST['password'])
        return obj
