from django import forms 
from datetime import datetime
  
# import GeeksModel from models.py 
from .models import ToDoList,date
  
# create a ModelForm 
class todoform(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = ToDoList
        fields = [
        'your_day',
        ]
        widgets = {
            'your_day': forms.Textarea(attrs={'rows':5, 'cols':57}),
        }
class tododate(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = ToDoList
        fields = [
        'your_day',
        ]
class DateInput(forms.DateInput):
    input_type = 'date'
class dateform(forms.ModelForm):

    class Meta:
        model = date
        fields = ['choose_date',]
        widgets = {
            'choose_date': DateInput(),
        }
