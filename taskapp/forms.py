from .models import Task
from django import forms

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'title',
                'placeholder': 'Введите название'
            }),
            'description': forms.Textarea(attrs={
                'class': 'description',
                'placeholder': 'Введите описание'
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'completed'
            })
        }
        
        error_messages = {
            'title': {
                'max_length': 'Слишком длинное название!',
            },
            
            'description': {
                'max_length': 'Слишком длинное название!',
            }
        }