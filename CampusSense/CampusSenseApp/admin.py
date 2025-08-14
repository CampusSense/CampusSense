from django.contrib import admin
from .models import LoginTable, Department, Course, Staff, Students, Notification, Complaint, Subject, CorrectionRequest


# Register your models here.
admin.site.register(LoginTable)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Students)
admin.site.register(Notification)
admin.site.register(Complaint)
admin.site.register(Subject)
admin.site.register(CorrectionRequest)
