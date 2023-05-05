from django.shortcuts import render
from .models import Exercise


# Create your views here.
def index_view(request):
    exerises = Exercise.objects.all()
    return render(request, 'mainapp/index.html', {'exerises': exerises})
