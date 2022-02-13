#I have created this File - mohammedsaif001

from string import punctuation
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze (request):
    # Get Text from User in the TextArea
    djText = request.POST.get('text','default')
    
    # Getting the status of checkbox
    removepunc = request.POST.get('removepunc','off')
    upperCase = request.POST.get('upperCase','off')
    removeNewLine = request.POST.get('removeNewLine','off')
    removeExtraSpace =request.POST.get('removeExtraSpace','off')
    charCounter =request.POST.get('charCount','off')
    
    punctuations = ''' 
    '~`!@#$%^&*()-_=+\|}{":?><,./;'[]\}
    '''
    
    
    
    if removepunc == "on":
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed=analyzed+char
        
        params = {'purpose': 'Removed Punctuation','analyzedText' : analyzed}
        djText = analyzed
        # return render(request,'analyze.html',params)
    
    if (upperCase == 'on'):
        analyzed = ""
        for char in djText:
                analyzed = analyzed + char.upper()
            
        params = {'purpose': 'UpperCase','analyzedText' : analyzed}
        djText = analyzed
        # return render(request,'analyze.html',params)
        
    if (removeNewLine == 'on'):
            analyzed = ""
            for char in djText:
                if char!="\n" and char!="\r":
                    analyzed = analyzed + char
            
            params = {'purpose': 'New Line Remover','analyzedText' : analyzed}
            djText = analyzed
            # return render(request,'analyze.html',params)
        
    if (removeExtraSpace == 'on'):
            analyzed = ""
            for index,char in enumerate(djText):
                if djText[index] == " " and djText[index+1] == " ":
                    pass
                else:
                    analyzed = analyzed + char
            
            params = {'purpose': 'Extra Space Remover','analyzedText' : analyzed}
            djText = analyzed
            # return render(request,'analyze.html',params)
        
    if (charCounter == 'on'):
            analyzed = ""
            count = 0
            for char in djText:
                count+=1
            
            message = f"{djText} has {count} character/s"
            params = {'purpose': 'Character Counter','analyzedText' : message}
                

    if (removepunc!='on' and removeNewLine!='on' and charCounter!="on" and removeExtraSpace!="on" and upperCase!="on"):
        return HttpResponse("Please Select an Operation and Try Again")
        
    
    return render(request,'analyze.html',params)