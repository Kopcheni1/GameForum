from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Article
from .forms import ArticleForm


class ArticlesList(ListView):
    model = Article
    ordering = '-dateCreation'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('articles.add_article')
    form_class = ArticleForm
    model = Article
    template_name = 'article_create.html'


class ArticleEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('articles.change_article')
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('articles.delete_article')
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles_list')
