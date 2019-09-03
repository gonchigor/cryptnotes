from django import forms
from .models import Category, Note


class CategoryForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Category


class NoteForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                "Введенные пароли не совпадают"
            )

    class Meta:
        model = Note
        fields = ['name', 'header', 'text', 'password', 'category']
        widgets = {
            'password': forms.PasswordInput,
            'category': forms.HiddenInput,
        }
