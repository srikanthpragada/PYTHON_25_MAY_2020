from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Book


class HelloView(TemplateView):
    template_name = 'hello.html'


class ListBooksView(ListView):
    model = Book
    # default context name is object_list
    context_object_name = 'books'  # name to be sent to template

