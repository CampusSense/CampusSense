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
        obj = Complaint.objects.all()
        return render(request, "admin module/complaints.html", {'val': obj})        

class ManageCourse(View):
    def get(self, request):
        obj = Course.objects.all()
        return render(request, "admin module/managecourse.html", {'val': obj})        

class ManageDept(View):
    def get(self, request):
        obj = Department.objects.all()
        return render(request, "admin module/managedept.html", {'val': obj})          

class ManageNotification(View):
    def get(self, request):
        obj = Notification.objects.all()
        return render(request, "admin module/managenotification.html", {'val': obj})   

class ManageStaff(View):
    def get(self, request):
        obj = Staff.objects.all()
        return render(request, "admin module/managestaff.html", {'val': obj})  

class ManageStudent(View):
    def get(self, request):
        obj = Students.objects.all()
        return render(request, "admin module/managestudent.html", {'val': obj}) 

class ManageSubjects(View):
    def get(self, request):
        obj = Subject.objects.all()
        return render(request, "admin module/managesubjects.html", {'val': obj}) 

class ViewProfile(View):
    def get(self, request):
        return render(request, "admin module/view profile.html") 


# ////////////////////////////////////////////////////// HOD  //////////////////////////////////////
class HodHome(View):
    def get(self, request):
        return render(request, "HOD module/hodhome.html") 
class ManageNotification1(View):
    def get(self, request):
        return render(request, "HOD module/manage notification.html")   

class ManageSubjects1(View):
    def get(self, request):
        return render(request, "HOD module/managesubjects.html")

class ViewNotification(View):
    def get(self, request):
        return render(request, "HOD module/view notification.html")  

class ViewProfile1(View):
    def get(self, request):
        return render(request, "HOD module/view profile.html") 
