from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Dharani'})


def add(request):
   firstname=request.GET['fname'] 
  
   lastname=request.GET['lname'] 
 
   address=request.GET['address'] 
 
   gender=request.GET['gender'] 
   
   val=firstname +" "+lastname+" "+address+" "+gender

   return render(request,'result.html',{'fname': firstname,'lname':lastname,'addr':address,'gender':gender})

