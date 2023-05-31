from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'mintu','age':6}
    return render(request,'wish.html',context=d)
def condition(request):
    d={'a':200,'b':40}
    return render(request,'condition.html',context=d)
def loop(request):
    d={'a':100,'b':202,'c':30}
    return render(request,'loop.html',context=d)
def loop1(request):
     d={'a':10,'b':20,'c':30}
     return render(request,'loop1.html',context=d)
def loop2(request):
    d={'name':'mounika'}
    return render(request,'loop2.html',context=d)
