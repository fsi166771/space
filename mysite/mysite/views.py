from django.http import HttpResponse

def myHelloWorld(request):
    return HttpResponse("Hello My Django!")