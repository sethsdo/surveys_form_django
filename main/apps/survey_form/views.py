from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request): 
  return render(request, 'temp/index.html')

def about(request):
  return redirect(request, 'result/')

def result(request):
    context = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment'],
    }
    return render(request, 'temp/about.html', context)


def back(request):
  return render(request, 'temp/index.html')
