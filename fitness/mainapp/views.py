from django.shortcuts import render
from .models import Exercise, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm


# Create your views here.
def index_view(request):
    exerises = Exercise.objects.all()
    return render(request, 'mainapp/index.html', {'exerises': exerises})


class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = '/category-list/'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/category-list/'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/category-list/'