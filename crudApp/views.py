from django.shortcuts import render , redirect
from django.http import HttpResponse
from crudApp.models import Student
from crudApp.forms import StudentForm

# Create your views here.

def retrieve_view(request):
    student = Student.objects.all()
    return render(request , 'crud.html' ,{'student' : student})


def create_view(request):
    Form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud')
    return render(request , 'create.html' , {'form':Form})


def delete_view(request , id):
    print(id)
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('crud')

def update_view(request , id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST , instance = student)
        if form.is_valid():
            form.save()
            return redirect('crud')

    return render(request , 'update.html' , {'student' : student})