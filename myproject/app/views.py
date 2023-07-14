from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import employee
# Create your views here.
def greet(request):
  return HttpResponse('hello i am learing') 

def index(request):
  emp=employee.objects.all()
  context={
    'emp':emp
    }
  return render(request,'index.html',context)

def add(request):
   if request.method=='POST':
     
      name=request.POST['name']
      email=request.POST['email']
      address=request.POST['address']
      phone=request.POST['phone']

  
      emp= employee(
         name=name,
         email=email,
         address=address,
         phone=phone,
      )
      emp.save()
      return redirect('home')
      return render(request,'index.html')
   
def edit(request):
   emp=employee.objects.all()
   context={
   'emp':emp
   }
   return redirect (request,'index.html',context)

def update(request,id):
   emp=employee.objects.all()
   if request.method=='POST':
     
      name=request.POST['name']
      email=request.POST['email']
      address=request.POST['address']
      phone=request.POST['phone']

  
      emp= employee(
         id=id,
         name=name,
         email=email,
         address=address,
         phone=phone,
      )
      emp.save()
      return redirect('home')
   
   
   return redirect (request,'index.html')

def delete(request,id):
   emp=employee.objects.filter(id=id)
   emp.delete()
   context={
      'emp':emp
   }
   return redirect('home')