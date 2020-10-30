from .models import Todo, Projects
from django import forms
import datetime


class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Type here a title for a task',
    'class':'form-control'}))
    
    class Meta:
        model=Projects
        fields = ("__all__")
   
class TodoForm(forms.ModelForm):
    completed = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    task = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Start typing here to create a task'}))
    deadline = forms.DateField(widget=forms.SelectDateWidget(years=range(datetime.date.today().year,
    datetime.date.today().year+2)))
        
    def __init__(self, *args, **kwargs):
        super(TodoForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})
        self.fields['priority'].widget.attrs.update({'id':'priority'})
        self.fields['task'].widget.attrs.update({'id':'task'})
       
    class Meta:
        model = Todo
        fields = ("__all__")

 