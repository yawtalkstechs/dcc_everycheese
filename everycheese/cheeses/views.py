from django.views.generic import (ListView, DetailView, 
            CreateView, UpdateView, DeleteView)

from .models import Cheese

# Create your views here.
class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseCreateView(CreateView):
    model = Cheese
    fields = ('name', 'description', 'firmness', 'country_of_origin')

class CheeseUpdateView(UpdateView):
    model = Cheese

class CheeseDeleteView(DeleteView):
    model = Cheese