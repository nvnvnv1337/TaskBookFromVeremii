from .models import Task
from django import forms

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        
        error_messages = {
            'title': {
                'max_length': 'Слишком длинное название!',
            }
            
        }