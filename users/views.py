from django.shortcuts import render
from .forms import RegistrationForm


def register(request):
    form = RegistrationForm(request.POST)
    return render(request, "users/register_volunteer.html", {"form": form})
