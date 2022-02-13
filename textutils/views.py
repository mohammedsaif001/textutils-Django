#I have created this File - mohammedsaif001

from string import punctuation
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze (request):
    djText = request.GET.get('text','default')
    print(djText)
    
    removep = request.GET.get('removepunc','off')
    print(removep)
    
    punctuations = ''' 
    '~`!@#$%^&*()-_=+\|}{":?><,./;'[]\}
    '''
    analyzed = ""
    
    if removep == "on":
        for char in djText:
            if char not in punctuations:
                analyzed=analyzed+char
        
        params = {'purpose': 'Removed Punctuation','analyzedText' : analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")