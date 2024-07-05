from django.http import HttpResponse

def saluda(request):
    return HttpResponse('Hola')