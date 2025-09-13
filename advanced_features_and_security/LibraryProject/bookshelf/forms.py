# bookshelf/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100)

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
