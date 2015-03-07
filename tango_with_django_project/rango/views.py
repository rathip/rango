from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)
##    return HttpResponse("Rango says hey there world! <br/> <a href='/rango/about'>About</a>")

def about(request):
    context_dict = {'aboutmessage': "I am about from the context"}
    return render(request, 'rango/about.html', context_dict)
##    return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>Index</a>")
