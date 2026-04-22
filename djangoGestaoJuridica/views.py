from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo ao sistema de gestão jurídica</h1>")