
from django.contrib import messages
from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView)

from .models import Author
# Create your views here.


class HomePage(TemplateView):
    template_name = 'home.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'authors.html'
    context_object_name = 'author_list'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name', ]

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Author created')
        form.save()
        return super().form_valid(form)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
