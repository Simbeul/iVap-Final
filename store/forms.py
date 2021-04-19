from django import forms
from django.shortcuts import render

from .models import ReminderEmail

class EmailForm(forms.ModelForm):
    class Meta:
        model = ReminderEmail
        fields = [
            'remindemail'
        ]