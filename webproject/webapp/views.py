from django.shortcuts import render
from . models import Tables
from  . models import  Place

# Create your views here.
def fun1(request):
    obj = Tables.objects.all()
    objj = Place.objects.all()
    return render(request,'index.html',{'obj1':obj,'obj2':objj})
