from django.forms import DateInput, ModelForm

from .models import Project, Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {'due_date': DateInput(format=('%Y-%m-%d'),
                                         attrs={'type': 'date'})
                                         }
        

class ProjectForm(ModelForm):
    class Meta:
        model = Project