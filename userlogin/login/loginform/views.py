from django.http import HttpResponse
from django.template import loader
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django .template import loader
from django.urls import reverse
from loginform.models import *
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from.models import New_Ticket
from loginform.models import New_Ticket

  
@ensure_csrf_cookie

def home(request):
    template = loader.get_template("signin.html")
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def Add (request):
  template = loader.get_template('redirect.html')
  return HttpResponse(template.render({}, request))

def manage (request):
  template = loader.get_template('manage.html')
  return HttpResponse(template.render({}, request))

def Add1 (request):
  mymembers = New_Ticket.objects.all().values()
  template = loader.get_template('manage.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

@csrf_exempt
def Addrecord(request):
   if request.method =="POST":
    email =request.POST["email"]
    upswd1 =request.POST["upswd1"]
    print(email,upswd1)
    ins = Login_form(email = email,upswd1=upswd1)
    ins.save()
    print("Data send Successfully")
    return HttpResponseRedirect(reverse('Add'))

@csrf_exempt
def ticket(request):
   if request.method =="POST":
       Name = request.POST["Name"]
       dept = request.POST["dept"]
       category = request.POST["category"]
       subject = request.POST["subject"]
       priority = request.POST["priority"]
       description = request.POST["description"]
       print(Name,dept,category,subject,priority,description)
       ins = New_Ticket(Name = Name,dept=dept,category=category,subject=subject,priority=priority,description=description)
       ins.save()
       print("Data send Successfully")
       return HttpResponseRedirect(reverse('Add1')) 