from django.shortcuts import render

# Create your views here.
def country(request):
    return render(request,'index.html')

def india(request):
    return render(request,'india.html')

def australia(request):
    return render(request,'australia.html')

def america(request):
    return render(request,'america.html')


def gujarat(request):
    return render(request,'gujarat.html')
def maharastra(request):
    return render(request,'maharastra.html')
def karnataka(request):
    return render(request,'karnataka.html')

def gandhinagar(request):
    return render(request,'gandhinagar.html')
def mumbai(request):
    return render(request,'mumbai.html')
def bengaluru(request):
    return render(request,'bengaluru.html')

def newsouthwales(request):
    return render(request,'newsouthwales.html')
def queensland(request):
    return render(request,'queensland.html')
def southaustralia(request):
    return render(request,'southaustralia.html')
def tsamnia(request):
    return render(request,'tsamnia.html')

def sydney(request):
    return render(request,'sydney.html')
def brisbane(request):
    return render(request,'brisbane.html')
def adelaide(request):
    return render(request,'adelaide.html')
def hobart(request):
    return render(request,'hobart.html')