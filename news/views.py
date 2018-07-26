from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Article

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_article_list'
    def get_queryset(self):
        """Return the last ten published article."""
        return Article.objects.order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    model = Article
    template_name = 'details.html'