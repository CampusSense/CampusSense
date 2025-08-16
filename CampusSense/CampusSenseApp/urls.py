"""
URL configuration for CampusSense project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from CampusSenseApp.views import *

urlpatterns = [
    path('', LoginPage.as_view(), name="LoginPage"),

    # //////////////////////////////////////////// ADMIN /////////////////////////////////////////
    path('Complaints', Complaints.as_view(), name="Complaints"),
    path('ManageCourse', ManageCourse.as_view(), name="ManageCourse"),
    path('ManageDept', ManageDept.as_view(), name="ManageDept"),
    path('ManageNotification', ManageNotification.as_view(), name="ManageNotification"),
    path('ManageStaff', ManageStaff.as_view(), name="ManageStaff"),
    path('ManageStudent', ManageStudent.as_view(), name="ManageStudent"),
    path('ManageSubjects', ManageSubjects.as_view(), name="ManageSubjects"),
    path('ViewProfile', ViewProfile.as_view(), name="ViewProfile"),
    path('AdminHome', AdminHome.as_view(), name="AdminHome"),

    # ///////////////////////////////////////////////// HOD  //////////////////////////////////////////
    path('HodHome', HodHome.as_view(), name="HodHome"),
    path('ManageNotification1', ManageNotification1.as_view(), name="ManageNotification1"),
    path('ManageSubjects1', ManageSubjects1.as_view(), name="ManageSubjects1"),
    path('ViewNotification', ViewProfile.as_view(), name="ViewNotification"),
    path('ViewProfile', ViewProfile.as_view(), name="ViewProfile"),

]
