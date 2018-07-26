from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Annonce

class JobsView(generic.ListView):
    model = Annonce
    template_name="jobs_list.html"

class JobsDetailView(generic.DetailView):
    model = Annonce
    template_name = 'jobs_details.html'