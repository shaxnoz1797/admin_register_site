from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')



@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    teachers = services.get_teachers()
    subjects = services.get_subject()
    groups = services.get_groups()
    students = services.get_students()
    kafedras = services.get_kafedra()
    ctx = {
        'counts': {
            'faculties': len(faculties),
            'kafedras':  len(kafedras),
            'groups':  len(groups),
            'students':  len(students),
            'subjects':  len(subjects),
            'teachers':  len(teachers),
        }
    }

    return  render(request,'index.html', ctx)


@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "form": form
    }
    return render(request, 'faculty/form.html',ctx)



# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url =  reverse_lazy("login_page")
#     template_name = "signup.html"


@login_required_decorator
def faculty_edit(request,pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'faculty/form.html',ctx)



@login_required_decorator
def faculty_delete(request,pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return  redirect('faculty_list')


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, 'faculty/list.html',ctx)



#************************************* KAFEDRA ******************************************

@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "form": form
    }
    return render(request, 'kafedra/form.html',ctx)


@login_required_decorator
def kafedra_edit(request,pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'kafedra/form.html',ctx)



@login_required_decorator
def kafedra_delete(request,pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return  redirect('kafedra_list')



@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedra()
    print(kafedras)
    ctx = {
        "kafedras": kafedras
    }
    return render(request, 'kafedra/list.html',ctx)


#******************************* groups *****************************************************
@login_required_decorator
def groups_create(request):
    model = Groups()
    form = GroupsForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('groups_list')
    ctx = {
        "form": form
    }
    return render(request, 'groups/form.html',ctx)



@login_required_decorator
def groups_edit(request,pk):
    model = Groups.objects.get(pk=pk)
    form = GroupsForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('groups_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'groups/form.html',ctx)



@login_required_decorator
def groups_delete(request,pk):
    model = Groups.objects.get(pk=pk)
    model.delete()
    return  redirect('groups_list')


@login_required_decorator
def groups_list(request):
    groups = services.get_groups()
    print(groups)
    ctx = {
        "groups": groups
    }
    return render(request, 'groups/list.html',ctx)


# ***************************** Student  *******************************************
@login_required_decorator
def students_create(request):
    model = Students()
    form = StudentsForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('students_list')
    ctx = {
        "form": form
    }
    return render(request, 'students/form.html',ctx)



@login_required_decorator
def students_edit(request,pk):
    model = Students.objects.get(pk=pk)
    form = StudentsForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('students_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'students/form.html',ctx)



@login_required_decorator
def students_delete(request,pk):
    model = Students.objects.get(pk=pk)
    model.delete()
    return  redirect('students_list')


@login_required_decorator
def students_list(request):
    students = services.get_students()
    print(students)
    ctx = {
        "students": students
    }
    return render(request, 'students/list.html',ctx)

# **************************************** Subject ***********************************************
@login_required_decorator
def subject_create(request):
    model = Subject()
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
            form = SubjectForm()

    return render(request, 'subject/form.html',{"form": form})

@login_required_decorator
def subject_edit(request,pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'subject/form.html',ctx)



@login_required_decorator
def subject_delete(request,pk):
    model = Subject.objects.get(pk=pk)
    model.delete()
    return  redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_subject()
    print(subjects)
    ctx = {
        "subjects": subjects
    }
    return render(request, 'subject/list.html',ctx)

# ************************************** Teachers ********************************************************
@login_required_decorator
def teachers_create(request):
    model = Teachers()
    form = TeachersForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teachers_list')
    ctx = {
        "form": form
    }
    return render(request, 'teachers/form.html',ctx)



@login_required_decorator
def teachers_edit(request,pk):
    model = Teachers.objects.get(pk=pk)
    form = TeachersForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teachers_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'teachers/form.html',ctx)



@login_required_decorator
def teachers_delete(request,pk):
    model = Teachers.objects.get(pk=pk)
    model.delete()
    return  redirect('teachers_list')


@login_required_decorator
def teachers_list(request):
    teachers = services.get_teachers()
    print(teachers)
    ctx = {
        "teachers": teachers
    }
    return render(request, 'teachers/list.html',ctx)
