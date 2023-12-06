from django.shortcuts import render,redirect
from .forms import CreateNewUser,Your_tasks
from django.contrib import messages
from .models import Task


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Your_tasks(request.POST)
        if form.is_valid():
            print('okk')
            name =  request.user.username
            print(name)
            task = form.save(commit=False)
            task.name = request.user
            task.save()
            messages.success(request,'Your Task is Saved')
            return redirect("home")
        else:
            print('nott')
            messages.error(request,'Your Task is not saved')
    form = Your_tasks()

    stu = Task.objects.all()
    return render(request,'home.html',{'form':form,'tasks':stu})

def deltask(request,pk):
    data = Task.objects.get(sno=pk)
    data.delete()
    messages.error(request,'Your task has been deleted')
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()   
            messages.success(request,'Your account has been created')    
            return redirect('home')     
        else:
            messages.error(request,'Please enter the correct values')
            return redirect('signup')
    form = CreateNewUser()       
    return render(request,'signup.html',{'form':form})