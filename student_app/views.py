from django.shortcuts import render, redirect,get_object_or_404
from .forms import StudentForm
from .models import Student

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print("hello")
            return redirect('all_students')
    else:
        form = StudentForm()

    return render(request, 'home.html', {'form': form})

def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html', {'students': students})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('all_students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_update.html', {'form': form, 'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('all_students')

    return render(request, 'student_delete.html', {'student': student})
