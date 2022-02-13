#I have created this File - mohammedsaif001

from string import punctuation
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze (request):
    # Get Text from User in the TextArea
    djText = request.GET.get('text','default')
    
    # Getting the status of checkbox
    removepunc = request.GET.get('removepunc','off')
    upperCase = request.GET.get('upperCase','off')
    removeNewLine = request.GET.get('removeNewLine','off')
    removeExtraSpace =request.GET.get('removeExtraSpace','off')
    charCounter =request.GET.get('charCount','off')
    
    punctuations = ''' 
    '~`!@#$%^&*()-_=+\|}{":?><,./;'[]\}
    '''
    analyzed = ""
    
    
    if removepunc == "on":
        for char in djText:
            if char not in punctuations:
                analyzed=analyzed+char
        
        params = {'purpose': 'Removed Punctuation','analyzedText' : analyzed}
        return render(request,'analyze.html',params)
    
    elif (upperCase == 'on'):
            for char in djText:
                analyzed = analyzed + char.upper()
            
            params = {'purpose': 'UpperCase','analyzedText' : analyzed}
            return render(request,'analyze.html',params)
        
    elif (removeNewLine == 'on'):
            for char in djText:
                if char!="\n":
                    analyzed = analyzed + char
            
            params = {'purpose': 'New Line Remover','analyzedText' : analyzed}
            return render(request,'analyze.html',params)
        
    elif (removeExtraSpace == 'on'):
            for index,char in enumerate(djText):
                if djText[index] == " " and djText[index+1] == " ":
                    pass
                else:
                    analyzed = analyzed + char
            
            params = {'purpose': 'Extra Space Remover','analyzedText' : analyzed}
            return render(request,'analyze.html',params)
        
    elif (charCounter == 'on'):
            count = 0
            for char in djText:
                count+=1
            
            message = f"{djText} has {count} character/s"
            params = {'purpose': 'Character Counter','analyzedText' : message}
            return render(request,'analyze.html',params)
                
    else:
        return HttpResponse("Error")