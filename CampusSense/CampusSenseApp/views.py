from django.shortcuts import render
from django.views import View
from CampusSenseApp.models import *
from django.http import HttpResponse
# Create your views here.

class LoginPage(View):
    def get(self, request):
        return render(request, "loginpage.html")
    def post(self,request):
        username1=request.POST['username']
        password1=request.POST['password']
        login_obj=LoginTable.objects.get(Username=username1,Password=password1)
        if login_obj.Usertype=='admin':
            return HttpResponse('''<script>alert("adminhome");window.location="/AdminHome";</script>''')
        elif login_obj.Usertype=='hod':
            return HttpResponse('''<script>alert("hodhome");window.location="/HodHome";</script>''')
# ////////////////////////////////////////// ADMIN /////////////////////////////////////////////
class AdminHome(View):
    def get(self, request):
        return render(request, "admin module/adminhome.html")        

class Complaints(View):
    def get(self, request):
        return render(request, "admin module/complaints.html")        

class ManageCourse(View):
    def get(self, request):
        return render(request, "admin module/managecourse.html")        

class ManageDept(View):
    def get(self, request):
        return render(request, "admin module/managedept.html")   

class ManageNotification(View):
    def get(self, request):
        return render(request, "admin module/managenotification.html")   

class ManageStaff(View):
    def get(self, request):
        return render(request, "admin module/managestaff.html")  

class ManageStudent(View):
    def get(self, request):
        return render(request, "admin module/managestudent.html") 

class ManageSubjects(View):
    def get(self, request):
        return render(request, "admin module/managesubjects.html") 

class ViewProfile(View):
    def get(self, request):
        return render(request, "admin module/view profile.html") 


# ////////////////////////////////////////////////////// HOD  //////////////////////////////////////
class HodHome(View):
    def get(self, request):
        return render(request, "HOD module/hodhome.html") 
class ManageNotification(View):
    def get(self, request):
        return render(request, "HOD module/manage notification.html")   

class ManageSubjects(View):
    def get(self, request):
        return render(request, "HOD module/managesubjects.html")

class ViewNotification(View):
    def get(self, request):
        return render(request, "HOD module/view notification.html")  

class ViewProfile(View):
    def get(self, request):
        return render(request, "HOD module/view profile.html") 
