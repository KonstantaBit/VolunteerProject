from django.shortcuts import render, redirect
from .forms import CreateNewTask
from .models import Task


def catalog(request):
    tasks = Task.objects.all()
    return render(request, "catalog/catalog.html", {'tasks': tasks})


def add_task(request):
    form = CreateNewTask()
    if request.method == 'POST':
        formed = CreateNewTask(request.POST, request.FILES)
        if formed.is_valid():
            name = formed.cleaned_data['name']
            description = formed.cleaned_data['description']
            award = int(formed.cleaned_data['award'])
            limiter = int(formed.cleaned_data['limiter'])
            photo = formed.cleaned_data['photo']

            task = Task(
                organization=request.user.organization,
                name=name,
                description=description,
                award=award,
                limiter=limiter,
                photo=photo
            )
            task.save()
            return redirect('/')
    return render(request, "catalog/create_new_task.html", {"form": form})
