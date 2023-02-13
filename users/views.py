from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import VolunteerRegistrationForm, ValidatorRegistrationForm, OrganizationRegistrationForm
from .models import Volunteer, Validator, Organization


def reg_volunteer(request):
    form = VolunteerRegistrationForm()
    if request.method == 'POST':
        formed = VolunteerRegistrationForm(request.POST)
        if formed.is_valid():
            user = formed.save()
            volunteer = Volunteer(user=user)
            volunteer.save()
            login(request, user)
            return redirect('/')
    return render(request, "users/register_volunteer.html", {"form": form})


def reg_validator(request):
    form = ValidatorRegistrationForm()
    if request.method == 'POST':
        formed = ValidatorRegistrationForm(request.POST)
        if formed.is_valid():
            user = formed.save()
            validator = Validator(user=user)
            validator.save()
            login(request, user)
            return redirect('/')
    return render(request, "users/register_validator.html", {"form": form})


def reg_organization(request):
    form = VolunteerRegistrationForm()
    if request.method == 'POST':
        formed = OrganizationRegistrationForm(request.POST)
        if formed.is_valid():
            user = formed.save()
            organization = Organization(user=user)
            organization.save()
            login(request, user)
            return redirect('/')
    return render(request, "users/register_organization.html", {"form": form})
