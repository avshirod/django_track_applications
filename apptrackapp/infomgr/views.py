from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return render(request, 'infomgr/index.html', context=dict())
    return HttpResponse('<h1>Ello There Matey</h1>')
