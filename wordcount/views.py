from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #render(request, template_name, context=None[a dictionary], content_type=None, status=None, using=None)
    return render(request,'home.html',{'key':'this is value'})

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext=request.GET['fulltext']
    l=fulltext.split()
    length=len(l)
    return render(request,'count.html',
    {
    'fulltext':fulltext,
    'length':length,
    })
