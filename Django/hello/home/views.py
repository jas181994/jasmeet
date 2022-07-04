from django.shortcuts import render,HttpResponse

def index(request):
  
   return render(request,'index.html')
   #return HttpResponse("Web page created by jasmeet using Django")

def about(request):
    return HttpResponse("This is about page")


def Field(request):
    return HttpResponse("This is a Web designing page")
# Create your views here.
