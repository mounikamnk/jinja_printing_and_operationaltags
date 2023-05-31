from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'mintu','age':6}
    return render(request,'wish.html',context=d)
def condition(request):
    d={'a':200,'b':40}
    return render(request,'condition.html',context=d)
