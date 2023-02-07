from django import forms
from django.core.exceptions import ValidationError

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'author',
            'title',
            'category',
            'text',
            'file',
        ]
        labels = {
            'author': 'Author',
            'title': 'Title',
            'category': 'Category',
            'text': 'Text',
            'file': 'File',
        }
