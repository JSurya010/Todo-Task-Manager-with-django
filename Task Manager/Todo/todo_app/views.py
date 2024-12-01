from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from todo_app.models import todo_list
from . import models



@login_required(login_url='/login')
def home(request):
    return render(request, 'signup.html')


def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psd')
        print(username,email,password)
        NewUser = User.objects.create_user(username,email,password)
        NewUser.save()
        return redirect('/login')
    return render(request,'signup.html') 


def Login(request):
    if request.method =='POST':
        name=request.POST.get('username')
        passd = request.POST.get('psd')
        print(name,passd)
        user =authenticate(request,username=name,password=passd)
        if user != None:
            login(request,user)
            return redirect('/tasklist')
        else:
            return redirect('/login')
    return render(request,'login.html')

def get_user_tasks(user):
    return todo_list.objects.filter(user=user).order_by('-task_created_date').values('id','task', 'start_date', 'end_date')


@login_required(login_url='/login')
def todolist(request):
    if request.method == "GET":
        tasks = get_user_tasks(request.user)
        return render(request, "todolist.html", {"res": tasks, "user": request.user})



@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        start_task = request.POST.get('startdate')
        end_task = request.POST.get('enddate')
        print(task_name,start_task,end_task)
        obj= models.todo_list(task=task_name,start_date=start_task,end_date=end_task,user=request.user)
        obj.save()
        user=request.user
        print(user)
        tasks = get_user_tasks(request.user)
        print(tasks)
        return redirect('/tasklist',{'response':tasks})

    tasks = get_user_tasks(request.user)
    return render(request,'todo.html',{'response':tasks})

def delete_todo(request,id):
    print(id)
    obj=models.todo_list.objects.get(id=id)
    obj.delete()
    return redirect('/tasklist')

@login_required(login_url='/loginn')
def edit_todo(request, id):
    
    if request.method == 'POST':
        title = request.POST.get('task')
        print(title)
        obj = models.todo_list.objects.get(id=id)
        obj.task = title
        obj.save()
        return redirect('/tasklist')

    obj = models.todo_list.objects.get(id=id)
    return render(request, 'edit_todo.html', {'obj': obj})


def signout(request):
    logout(request)
    return redirect('/login')





# from django.shortcuts import redirect, render
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from todo_app.models import todo_list


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('psd')
#         User.objects.create_user(username=username, email=email, password=password).save()
#         return redirect('/login')
#     return render(request, 'signup.html')


# def Login(request):
#     if request.method == 'POST':
#         name = request.POST.get('username')
#         password = request.POST.get('psd')
#         user = authenticate(request, username=name, password=password)
#         if user:
#             login(request, user)
#             return redirect('/todolist')
#         else:
#             return redirect('/login')
#     return render(request, 'login.html')


# def signout(request):
#     logout(request)
#     return redirect('/login')


# @login_required(login_url='/login')
# def todolist(request):
#     tasks = todo_list.objects.filter(user=request.user).order_by('-task_created_date')
#     return render(request, 'todolist.html', {"res": tasks})


# @login_required(login_url='/login')
# def todo(request):
#     if request.method == 'POST':
#         task_name = request.POST.get('task')
#         start_date = request.POST.get('startdate')
#         end_date = request.POST.get('enddate')
#         todo_list.objects.create(task=task_name, start_date=start_date, end_date=end_date, user=request.user)
#         return redirect('/todolist')
#     return render(request, 'todo.html')


# @login_required(login_url='/login')
# def edittodo(request, id):
#     task = todo_list.objects.get(id=id, user=request.user)
#     if request.method == 'POST':
#         task.task = request.POST.get('task')
#         task.start_date = request.POST.get('startdate')
#         task.end_date = request.POST.get('enddate')
#         task.save()
#         return redirect('/todolist')
#     return render(request, 'edit_todo.html', {"task": task})


# @login_required(login_url='/login')
# def delete_todo(request, id):
#     todo_list.objects.filter(id=id, user=request.user).delete()
#     return redirect('/todolist')
