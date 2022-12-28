from django.http import HttpResponse
from django.shortcuts import render



def analyzer(request):
    getTexts = request.GET.get('text', 'default')
    getValueOfCheck = request.GET.get('removepunc', 'off')
    getValueOfUpper = request.GET.get('fullCapital', 'off')
    getValueOfLower = request.GET.get('fullSmall', 'off')
    getValueOfRemoveNL = request.GET.get('newLineRemoval', 'off')
    print(getTexts)
    print(getValueOfCheck)
    punctuationLists = ''',./':";?`-_{}[]()*&%$#@!+^'''
    filteredText = ""
    if getValueOfCheck == "on":
        for char in getTexts:
            if char not in punctuationLists:
                filteredText = filteredText+char
        counter = len(filteredText)
        params = {'Strings': getTexts, 'isCleared': filteredText,'count':counter}

    elif (getValueOfUpper == "on"):
        for char in getTexts:
            if char not in punctuationLists:
                filteredText = filteredText+char.upper()
        counter = len(filteredText)
        params = {'Strings': getTexts,
                  'isCleared': "Converted to Uppercase : "+filteredText,'count':counter}
        return render(request, 'analyze.html', params)
    elif (getValueOfLower == "on"):
        for char in getTexts:
            if char not in punctuationLists:
                filteredText = filteredText+char.lower()
        counter = len(filteredText)
        params = {'Strings': getTexts,
                  'isCleared': "Converted to Uppercase : "+filteredText,'count':counter}
        return render(request, 'analyze.html', params)
    elif(getValueOfRemoveNL == "on"):
        for char in getTexts:
            if char not in punctuationLists and char !="\n":
                filteredText = filteredText+ char.upper()
            counter = len(filteredText)
        params={'Strings': getTexts,
                  'isCleared': "Removed New Line : "+filteredText, 'count':counter}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error!")
    return render(request, 'analyze.html', params)
def home(request):
    return render(request,'index.html')