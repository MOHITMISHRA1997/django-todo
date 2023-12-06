from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

PRIORITY_CHOICES = (
    ('Hight Priority', 'Hight Priority'),
    ('Medium', 'Medium'),
    ('Basic', 'Basic'),
)

class Your_tasks(forms.ModelForm):
    your_task = forms.CharField(max_length=150,required=True)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    
    class Meta:
        model = Task
        fields = ['your_task', 'priority', 'posted_date']