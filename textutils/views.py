#I have created this File - mohammedsaif001

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # return HttpResponse("<h1>Home</h1>")

def removePunc (request):
    # Get Text from the User from webPage
    djText = request.GET.get('text','default')
    print(djText)
    return HttpResponse('Remove Punctuation')

def capitalize (request):
    return HttpResponse('Capitalize First Letter')

def newlineremove (request):
    return HttpResponse('newlineremove')

def spaceremove (request):
    return HttpResponse('space remove')

def charcount (request):
    return HttpResponse('charcount')



