#I have created this File - mohammedsaif001

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':"saif",'learning':'Django'}
    return render(request,'index.html',params)
    # return HttpResponse("<h1>Home</h1>")

def removePunc (request):
    return HttpResponse('Remove Punctuation')

def capitalize (request):
    return HttpResponse('Capitalize First Letter')

def newlineremove (request):
    return HttpResponse('newlineremove')

def spaceremove (request):
    return HttpResponse('space remove')

def charcount (request):
    return HttpResponse('charcount')



