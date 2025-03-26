from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Private

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EventForm(forms.ModelForm):
    class Meta:
        model = Private
        fields = ['title', 'name', 'category', 'adress', 'date', 'phone', 'price', 'image', 'discription']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'placeholder': '0'}),
            'discription': forms.Textarea(attrs={'rows': 5}),
        }

