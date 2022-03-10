from django.http import HttpResponse
def home(request):
    return HttpResponse('Hello World coding!!')

def index(request):
    fp=open(r'F:\django\project1\pro1\index.html','r')
    temp=fp.read()
    return HttpResponse(temp)