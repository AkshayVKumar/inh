from django.shortcuts import render
from app import forms
from app.models import Model_img
# Create your views here.

def sam(request):
    form=forms.from_demo()
    if request.method=='POST':
        form=forms.from_demo(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'img.html',context={'form':form,'data':"hello world"})

def disp(request):
    data=Model_img.objects.all()
    return render(request,'disp.html',context={'objects':data})

