from django.contrib import admin
from crudApp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list = ['student_no' , 'student_name' , 'student_class' , 'student_address']
    

admin.site.register(Student , StudentAdmin)