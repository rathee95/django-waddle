from django import forms
from .models import Question

class QuestionCreateForm(forms.ModelForm):
    # title = forms.CharField(max_length=8)
    # text = forms.Textfield(max_length=300)
    
    class Meta:
        model = Question
        fields = ['title', 'text']
