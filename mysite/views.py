from unicodedata import name
from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse('<h1> This is a TEST <h1>')
def json_test(request):
    return JsonResponse({'name':'Sadegh'})