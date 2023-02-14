from django.shortcuts import render, redirect
from .forms import CreateNewTask
from .models import Task


def catalog(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        if request.POST.get("take"):
            task = Task.objects.get(id=int(request.POST.get("take")) - 1,)
            task.users.add(request.user.volunteer)
            task.save()
    return render(request, "catalog/catalog.html", {'tasks': tasks})


def add_task(request):
    form = CreateNewTask()
    if request.method == 'POST':
        formed = CreateNewTask(request.POST, request.FILES)
        if formed.is_valid():
            name = formed.cleaned_data['name']
            description = formed.cleaned_data['description']
            award = int(formed.cleaned_data['award'])
            photo = formed.cleaned_data['photo']

            task = Task(
                organization=request.user.organization,
                name=name,
                description=description,
                award=award,
                photo=photo
            )
            task.save()
            return redirect('/')
    return render(request, "catalog/create_new_task.html", {"form": form})


def task(request, id):
    c_task = Task.objects.get(id=id)
    return render(request, 'catalog/task.html', {'task': c_task})