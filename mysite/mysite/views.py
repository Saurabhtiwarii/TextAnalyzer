from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return(render(request, 'index.html'))

def analyze(request):

    #get the text
    djtext = request.POST.get('text', 'default')
    capitalize = request.POST.get('fullcaps', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    newlinerem = request.POST.get('newlineremover', 'off')
    extraspacerem = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
    if(capitalize=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
    if (newlinerem == 'on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        djtext = analyzed

    if (extraspacerem == "on"):

        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        djtext = analyzed

    if capitalize !='on' and removepunc!='on' and newlinerem!='on' and extraspacerem!='on':
            return HttpResponse("Error")
    params = {'analyzed_text': djtext}
    return render(request, 'analyze.html', params)

