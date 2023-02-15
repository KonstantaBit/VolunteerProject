import django.contrib.auth.models
from django.contrib.auth import login
from django.shortcuts import render, redirect

from catalog.models import Task
from store.models import Benefit
from .forms import VolunteerRegistrationForm, ValidatorRegistrationForm, OrganizationRegistrationForm
from .models import Volunteer, Validator, Organization, User


def reg_volunteer(request):
    form = VolunteerRegistrationForm()
    if request.method == 'POST':
        formed = VolunteerRegistrationForm(request.POST)
        if formed.is_valid():
            user = formed.save()
            volunteer = Volunteer(user=user,)
            volunteer.save()
            login(request, user)
            return redirect('/')
    return render(request, "users/register_volunteer.html", {"form": form})


def reg_validator(request):
    return redirect('/')
    # form = ValidatorRegistrationForm()
    # if request.method == 'POST':
    #     formed = ValidatorRegistrationForm(request.POST)
    #     if formed.is_valid():
    #         user = formed.save()
    #         validator = Validator(user=user)
    #         validator.save()
    #         login(request, user)
    #         return redirect('/')
    # return render(request, "users/register_validator.html", {"form": form})


def reg_organization(request):
    form = OrganizationRegistrationForm()
    if request.method == 'POST':
        formed = OrganizationRegistrationForm(request.POST)
        if formed.is_valid():
            user = formed.save()
            organization = Organization(user=user)
            organization.save()
            login(request, user)
            return redirect('/')
    return render(request, "users/register_organization.html", {"form": form})


def personal_account(request, id):
    user = User.objects.get(id=id)
    try:
        tasks = Task.objects.filter(organization=user.organization)
    except BaseException:
        tasks = []
    try:
        tasks_to_u = Task.objects.filter(users=user.volunteer)
        benefits = Benefit.objects.all()
        if request.method == "POST":
            if request.POST.get("buy"):
                benefit = Benefit.objects.get(id=int(request.POST.get("buy")))
                user.volunteer.points -= benefit.cost
                user.volunteer.benefits.add(benefit)
                user.volunteer.save()
            if request.POST.get("cancel"):
                task = Task.objects.get(id=int(request.POST.get("cancel")))
                task.users.remove(user.volunteer)
    except BaseException:
        benefits = []
        tasks_to_u = []
    return render(request, 'users/personal_account.html', {'account_user': user,
                                                           'tasks': tasks,
                                                           'tasks_to_u': tasks_to_u,
                                                           'benefits': benefits,
                                                           })


def EditProfile(request):
    return redirect('/')
