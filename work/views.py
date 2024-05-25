from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import Register,Login_form,Task_form
from work.models import User,Task_model
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,**kwargs)
    return wrapper

def signin_must(fn):
    def wrapper(request,**kwargs):
        id=kwargs.get("pk")
        obj=Task_model.objects.get(id=id)
        if obj.user != request.user:
            return redirect("login")
        else:
            return fn(request,**kwargs)
    return wrapper

class Registration_view(View):
    def get(self,request):
        form=Register()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,**kwargs):
        form=Register(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            form=Register()
        return redirect("login")
    
class Login_view(View):
    def get(self,request,**kwargs):
        form=Login_form()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,**kwargs):
        form=Login_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(username=u_name,password=pwd)
            if user_obj:
                print("Login successfull")
                login(request,user_obj)
                return redirect("task")
            else:
                print("incorrect credentials")
                form=Login_form()
                return render(request,"login.html",{"form":form})
@method_decorator(signin_required,name="dispatch")           
class Add_taskview(View):
    def get(self,request,**kwargs):
        form=Task_form()
        data=Task_model.objects.filter(user=request.user).order_by("completed")
        return render(request,"task.html",{"form":form,"data":data})
    
    def post(self,request,**kwargs):
        form=Task_form(request.POST)   
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.success(request,"Task added successfully")
            form=Task_form()
        data=Task_model.objects.filter(user=request.user).order_by("completed")
        return render(request,"task.html",{"form":form,"data":data})
@method_decorator(signin_required,name="dispatch")
@method_decorator(signin_must,name="dispatch")

class delete_taskview(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        Task_model.objects.get(id=id).delete()
        form=Task_form()
        return redirect("task")
        
class task_editview(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        obj=Task_model.objects.get(id=id)
        if obj.completed==False:
            obj.completed=True
            obj.save()
            return redirect("task")
        else:
            obj.completed=False
            obj.save()
            return redirect("task")

    
class logout_view(View):
    def get(self,request):
        logout(request)
        return redirect("login")
    
@method_decorator(signin_required,name="dispatch")
@method_decorator(signin_must,name="dispatch")
class Taskupdate_view(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Task_model.objects.get(id=id)
        form=Task_form(instance=data)
        return render(request,"update.html",{"form":form})
    
    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Task_model.objects.get(id=id)
        form=Task_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
        form=Task_form()
        return redirect("task")
    
class Delete_userview(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        User.objects.get(id=id).delete()
        return redirect("login")
    
class Edit_userview(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=User.objects.get(id=id)
        form=Register(instance=data)
        return render(request,"edit_user.html",{"form":form})
    
    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=User.objects.get(id=id)
        form=Register(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("task")


class Firstpage_view(View):
    def get(self,request,**kwargs):
        return render(request,"firstpage.html")