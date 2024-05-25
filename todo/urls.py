"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from work.views import Registration_view,Login_view,Add_taskview,delete_taskview,task_editview,logout_view,Taskupdate_view,Delete_userview,Edit_userview
from work.views import Firstpage_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',Registration_view.as_view(),name="reg"),
    path('login/',Login_view.as_view(),name="login"),
    path('task/',Add_taskview.as_view(),name="task"),
    path("delete/<int:pk>",delete_taskview.as_view(),name="delete"),
    path("task/update/<int:pk>",task_editview.as_view(),name="update"),
    path("logout/",logout_view.as_view(),name="logout"),
    path("update1/<int:pk>",Taskupdate_view.as_view(),name="update1"),
    path("del/<int:pk>",Delete_userview.as_view(),name="del"),
    path("edit/<int:pk>",Edit_userview.as_view(),name="edit"),
    path('',Firstpage_view.as_view(),name="first"),
    path("api/",include("api.urls")),


]
