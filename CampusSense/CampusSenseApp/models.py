from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username=models.CharField(max_length=50,null=True, blank=True)
    Password=models.CharField(max_length=50,null=True, blank=True)
    Usertype=models.CharField(max_length=50,null=True, blank=True)

class Department(models.Model):
    DepartmentName=models.CharField(max_length=50,null=True, blank=True)

class Course(models.Model):
    CourseName=models.CharField(max_length=50, null=True,blank=True)     
    CourseCredit=models.FloatField(max_length=50,null=True,blank=True)
    CreatedDate=models.DateField(auto_now=True,null=True,blank=True)   

class Staff(models.Model):  
    StaffName=models.CharField(max_length=50,null=True,blank=True)
    Gender=models.CharField(max_length=50,null=True,blank=True)  
    DateofBirth=models.DateField(auto_now=True,null=True,blank=True)
    Designation=models.CharField(max_length=50,null=True,blank=True)
    Email=models.CharField(max_length=50,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    JoinDate=models.DateField(auto_now=True,null=True,blank=True)
    ProfileImage=models.FileField(null=True,blank=True)

class Students(models.Model):  
    Name=models.CharField(max_length=50,null=True,blank=True)
    RollNumber=models.CharField(max_length=50,null=True,blank=True)
    Gender=models.CharField(max_length=50,null=True,blank=True)  
    DateofBirth=models.DateField(auto_now=True,null=True,blank=True)
    Semester=models.CharField(max_length=50,null=True,blank=True)
    Email=models.CharField(max_length=50,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    Address=models.CharField(max_length=50,null=True,blank=True)
    AdmissionDate=models.DateField(auto_now=True,null=True,blank=True)
    ProfileImage=models.FileField(null=True,blank=True)   

class Notification(models.Model):
    Title=models.CharField(max_length=50,null=True,blank=True)     
    Message=models.Field(max_length=150,null=True,blank=True)
    CreatedDate=models.DateField(auto_now=True,null=True,blank=True)  
    ExpiryDate=models.DateField(auto_now=True,null=True,blank=True) 

class Complaint(models.Model):
    ComplaintType=models.CharField(max_length=50,null=True,blank=True)     
    Subject=models.Field(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=150,null=True,blank=True)  
    AssignedTo=models.CharField(max_length=50,null=True,blank=True)
    CreatedDate=models.DateField(auto_now=True,null=True,blank=True)  
    ResolvedDate=models.DateField(auto_now=True,null=True,blank=True)  

class Subject(models.Model):
    SubjectName=models.CharField(max_length=50,null=True,blank=True)     
    Semester=models.Field(max_length=100,null=True,blank=True)
    Type=models.CharField(max_length=150,null=True,blank=True)  
    
class CorrectionRequest(models.Model):
    RequestType=models.CharField(max_length=50,null=True,blank=True)     
    Description=models.CharField(max_length=150,null=True,blank=True)  
    CreatedDate=models.DateField(auto_now=True,null=True,blank=True)  
    ResolvedDate=models.DateField(auto_now=True,null=True,blank=True)  
                    