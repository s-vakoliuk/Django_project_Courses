from django.shortcuts import render# Create your views here.
from django.http import HttpResponse
from .models import Course



def index(request):
    courses=Course.objects.all()
    return render (request, 'courses.html', {'courses':courses})
