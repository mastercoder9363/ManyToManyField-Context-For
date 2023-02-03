from django.shortcuts import render
from .models import *

def index(request):
    postlar = Post.objects.all()
    context = {
        'postlar': postlar
    }
    return render(request, 'index.html', context)