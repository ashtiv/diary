from django.shortcuts import get_object_or_404,render, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages 
from .forms import todoform,dateform
from django.shortcuts import redirect
from django.conf import settings
# Create your views here.
# import datetime
from datetime import datetime
from .models import ToDoList
from .forms import todoform,tododate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import logging
import pprint
import collections


# Put the logging info within your django view
pp = pprint.PrettyPrinter(indent=4)
d=datetime.now().date()

logger = logging.getLogger(__name__)

def handler404(request,exception):
    # response = render_to_response(template_name)
    # response.status_code = 404
    # return HttpResponseRedirect("/error/err")
    context={}
    context['error']="Some error has occured"
    return render(request,"accounts/base.html",context)
def handler500(request):
    # response = render_to_response(template_name)
    # response.status_code = 500
    # return HttpResponseRedirect("/error/err")
    context={}
    context['error']="Some error has occured"
    return render(request,"accounts/base.html",context)
def handler403(request,exception):
    # response = render_to_response(template_name)
    # response.status_code = 500
    # return HttpResponseRedirect("/error/err")
    context={}
    context['error']="Some error has occured"
    return render(request,"accounts/base.html",context)
def handler400(request,exception):
    # response = render_to_response(template_name)
    # response.status_code = 500
    # return HttpResponseRedirect("/error/err")
    context={}
    context['error']="Some error has occured"
    return render(request,"accounts/base.html",context)
@login_required
def diary(request):
    k=ToDoList.objects.filter(user=request.user)
    lenn=len(k)
    context ={} 
    context['data']={};
    if(lenn>0):
        tt=0
        for jj in k:
            # a={str(jj.dardate):jj.id}
            context['data'][str(jj.dardate)]=jj.id
            tt=tt+1;
        # context['data']=kk
        context['data']=collections.OrderedDict(sorted(context['data'].items())[::-1])

    else :
        context['data']="Your haven't written yet."
    formd=dateform(request.POST or None)
    if request.method == "POST":
       if formd.is_valid():
          kd=formd.cleaned_data['choose_date']
          dd=kd
          kd=ToDoList.objects.filter(dardate=kd,user=request.user)
          if (len(kd)<=0):
            
            return HttpResponseRedirect("/new/"+str(dd))   
          kd=kd[0].id
          return HttpResponseRedirect("/"+str(kd))
          pp.pprint(kd)
          

          # ss.delete()
    # context['d']=d
    
    return render(request,'accounts/diary.html',{"context":context,"formd":formd})
@login_required
def newdate(request,dd):
    form=todoform(request.POST or None)
    # yed=""
    if form.is_valid():
          profile=form.save(commit = False)
          profile.user=request.user
          profile.dardate=dd
          profile.save()
          return HttpResponseRedirect("/wholediary")
    yed=str(dd)
    return render(request,'accounts/new.html',{"form":form,"yed":yed})
@login_required
def first(request):
    k=ToDoList.objects.filter(dardate=d,user=request.user)
    lenn=len(k)
    context ={} 
    context['d']=d
    if(lenn>0):
        kk=k[lenn-1].your_day
        context['data']=kk

    else :
        context['data']="Your today's writing is empty."
    return render(request,'accounts/home.html',{"context":context})
@login_required
def index(request):
    context ={} 
  
    # fetch the object related to passed id 
    k=ToDoList.objects.filter(dardate = datetime.now().date(),user=request.user)
    if(len(k)>0):
        obj = get_object_or_404(k, dardate = datetime.now().date()) 
        form = todoform(request.POST or None,instance = obj)
    else :
        form=todoform(request.POST or None)
  
    # pass the object as instance in form 
     
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        profile=form.save(commit = False) 
        profile.user=request.user
        profile.save()
        return HttpResponseRedirect("/"+str(profile.id)) 
  
    # add form dictionary to context 
    context["form"] = form
    context["yed"]=d; 
  
    return render(request, "accounts/update_view.html", context) 
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'accounts/home.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)
@login_required
def detail_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
   
    # add the dictionary during initialization 
    context["data"] = ToDoList.objects.get(id = id) 
    context["kkk"]=id
           
    return render(request, "accounts/detail_view.html", context) 
  
# update view for details 
@login_required
def update_view(request, id):
    # dictionary for initial data with  
    # field names as keys 
    context ={}
  
    # fetch the object related to passed id 
    obj = get_object_or_404(ToDoList, id = id)
    yedo=ToDoList.objects.filter(id=id)
    if(len(yedo)>0): 
        yed=str(ToDoList.objects.filter(id=id)[0].dardate)
    else :
        yed=""
  
    # pass the object as instance in form 
    form = todoform(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id) 
  
    # add form dictionary to context 
    context["form"] = form 
    context["yed"]=yed
    pp.pprint(yed)
  
    return render(request, "accounts/update_view.html", context)
@login_required
def delo(request,id):
    kkk=ToDoList.objects.filter(id=id).delete()
    # messages.info(request, 'Deleted successfully')
    return HttpResponseRedirect("/delsuccess/"+str(id))
@login_required
def dels(request,id):
    k=ToDoList.objects.filter(user=request.user)
    lenn=len(k)
    context ={} 
    context['msg']="Your entry deleted successfully"
    context['data']={};
    if(lenn>0):
        tt=0
        for jj in k:
            # a={str(jj.dardate):jj.id}
            context['data'][str(jj.dardate)]=jj.id
            tt=tt+1;
        # context['data']=kk
        context['data']=collections.OrderedDict(sorted(context['data'].items())[::-1])

    else :
        context['data']="Your haven't written yet."
    formd=dateform(request.POST or None)
    if request.method == "POST":
       if formd.is_valid():
          kd=formd.cleaned_data['choose_date']
          dd=kd
          kd=ToDoList.objects.filter(dardate=kd,user=request.user)
          if (len(kd)<=0):
            
            return HttpResponseRedirect("/new/"+str(dd))   
          kd=kd[0].id
          return HttpResponseRedirect("/"+str(kd))
          pp.pprint(kd)
          

          # ss.delete()
    # context['d']=d
    
    return render(request,'accounts/diary.html',{"context":context,"formd":formd})
@login_required
def error(request):
    context={}
    context['error']="Some error has occured"
    return render(request,"accounts/base.html",context)