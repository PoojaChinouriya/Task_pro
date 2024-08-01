from django import forms
from .models import Todo_Task

Status = [('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Cancel', 'Cancel'), ('Pending', 'Pending')]


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_Task
        fields = ['task_name', 'task_description', 'task_deadline']

        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'task_description': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'task_status': forms.Select(choices=Status, attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'task_deadline': forms.DateInput(attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'task_created_date': forms.DateInput(attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'task_completed_date': forms.DateInput(attrs={
                'class': 'form-control bg-dark text-light'
            })
        }


class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo_Task
        fields = ['task_name', 'task_description', 'task_status', 'task_deadline']


class StatusForm(StatusUpdateForm):
    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        self.fields['task_name'].widget.attrs['readonly'] = True
        self.fields['task_description'].widget.attrs['readonly'] = True
        self.fields['task_deadline'].widget.attrs['readonly'] = True