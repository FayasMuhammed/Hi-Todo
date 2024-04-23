from django import forms
from work.models import User,Task_model

class Register(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]
        widgets={
            'username':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Username"}),
            'first_name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your First Name"}),
            'last_name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Last Name"}),
            'email':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Email"}),
            'password':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Password"})
            }


class Task_form(forms.ModelForm):
    class Meta:
        model=Task_model
        fields=["task_name","task_description"]
        widgets={
            'task_name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter a new task"}),
            'task_description':forms.Textarea(attrs={"class":"form-control",'column':20,'rows':5,"placeholder":"Enter a description"})
            }

class Login_form(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your username"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your password"}))
    
    
