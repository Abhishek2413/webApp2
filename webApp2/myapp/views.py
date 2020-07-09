from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/show_view')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)
                return redirect('login')
        context = {'form':form}
        return render(request,'register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/show_view')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/show_view')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request,'login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def welcome(request):
    return render(request,"welcome.html")

@login_required(login_url='login')
def load_form(request):
    form = EmployeeForm
    return render(request, "index.html",{'form':form})

@login_required(login_url='login')
def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/show_view')

@login_required(login_url='login')
def show_view(request):
    emp = Employee.objects.all()  # retrive operation
    return render(request,'show.html',{'emp':emp})

@login_required(login_url='login')
def edit(request,id):
    emp = Employee.objects.get(id=id)
    return render(request,'edit.html',{'emp':emp})

@login_required(login_url='login')
def update(request,id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=emp)
    form.save()
    return redirect('/show_view')

@login_required(login_url='login')
def delete(request,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/show_view')

@login_required(login_url='login')
def search(request):
    given_name = request.POST['name']
    emp = Employee.objects.filter(ename__icontains=given_name)
    return render(request,'show.html',{'emp':emp})

