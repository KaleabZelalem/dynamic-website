from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def home(request):
    movies = Movie.objects.all()
    data = {'movies': movies}
    return render(request, 'home.html', data)

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def movies(request):
    return HttpResponse('movies page')

