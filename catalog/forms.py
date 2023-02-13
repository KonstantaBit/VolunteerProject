from django import forms
from .models import Task


class CreateNewTask(forms.Form):
    name = forms.CharField(label='Наименование', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}),)
    description = forms.CharField(
        label='Описание',
        max_length=1024,
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        ),
    )
    award = forms.CharField(
        label='Общее вознаграждение',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Целое положительное число'}
        )
    )
    limiter = forms.CharField(
        label='Лимит участников',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Целое положительное число'}
        )
    )

    photo = forms.ImageField(
        label='Превью',
    )


class EditTask(forms.Form):
    pass
