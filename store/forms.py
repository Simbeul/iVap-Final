from django import forms
from django.forms import ModelForm
from django.shortcuts import render

from .models import models, ReminderEmail

class EmailForm(forms.ModelForm):
    class Meta:
        model = ReminderEmail
        fields = ['remindemail', 'product']
        widgets = {
             'product': forms.HiddenInput()
        }