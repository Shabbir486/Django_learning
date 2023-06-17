from django.http import HttpResponse
from django.shortcuts import render


# Lecture 5
def index (request) :
    #Get the text
    textRecieved=(request.GET.get('text','default'))
    
    #Analyze the text
    print(textRecieved)
    return HttpResponse("Hello World")


# Lecture 6 -Creating personal navigator
def personalNavigator (req) :
    return HttpResponse('''
    <h1>Shabbir</h1>
    <a href="https://www.youtube.com/watch?v=AepgWsROO4k">Django code with Harry</a>''')


# Lecture 7- Laying the pipeline
def about (req) :
    return HttpResponse("Myself Shabbir")


# Lecture-8- Templates in Django
# --goto settings.py and add 'DIRS':['templates'],
# create a folder templates in main dir where manage.py is placed
# Then create a html template inside that and in views.py 'from django.shortcuts import render'
def template (req) :
    # Passing parameter to our HTML page(Check in template)
    params={'name':'Shabbir Ali','place':'Bokaro Steel City'}
    return render(req , 'analyze.html',params)

# Lecture 9-Creating Homepage for our learning test website
def testWebsite(request):
    # Check the index function
    return render(request,'test.html')

# Lecture 10 -Creating our first website
def analyze(request):
    # recText=request.GET.get('text','default')
    # # Check checkbox values
    # removepunc = request.GET.get ( 'removepunc' , 'off' )
    # fullcaps = request.GET.get ( 'fullcaps' , 'off' )
    # newlineremover = request.GET.get ( 'newlineremover' , 'off' )
    # extraspaceremover = request.GET.get ( 'extraspaceremover' , 'off' )

    recText = request.POST.get ( 'text' , 'default' )
    # Check checkbox values
    removepunc = request.POST.get ( 'removepunc' , 'off' )
    fullcaps = request.POST.get ( 'fullcaps' , 'off' )
    newlineremover = request.POST.get ( 'newlineremover' , 'off' )
    extraspaceremover = request.POST.get ( 'extraspaceremover' , 'off' )

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in recText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        recText = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in recText:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        recText = analyzed
        # return render(request, 'analyze.html', params)
    if (newlineremover == "on"):
        analyzed = ""
        for char in recText:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        recText = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(recText):
            if not (recText[index] == " " and recText[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        recText = analyzed
        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

# Lecture 13
def testBootstrap(request):
    # Check the index function
    return render(request,'test2.html')

# Lecture 16
# In django-it supports CSRF functionality i.e Cross-site Request Forgery (CSRF). Suppose somebody is using mySite and i created a url /delete for deleting my account.
# But if by Mistake i link that url somewhere that is loop Hole for that we need to use CSRF token
# which will verify that the end authorized user is sending that request
def testPostMapping(request):
    # Check the index function
    return render(request,'test3.html')

# Lecture 17
# Fixing the bugs in our demo website like 2 functions works simultaneously



