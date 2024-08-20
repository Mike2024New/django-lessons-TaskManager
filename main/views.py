from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context ={
        'title':'Главная страница',
        'tasks':tasks
    }
    return render(request, 'main/index.html',context)

def about(request):
    context ={
        'title':'Про сайт',
    }
    return render(request, 'main/about.html',context)

def create(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
        else:
            error = "Форма была не верной, возникла ошибка."
    form = TaskForm()
    context ={
        'title':'Добавить задачу',
        'form':form,
        'erorr': error,
    }
    return render(request, 'main/create.html',context)