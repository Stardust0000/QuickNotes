from django import forms
from .models import Notes
import re
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields=['text']
        widgets = {
            "text" : forms.TextInput(attrs={
                "class":"txtarea",
                "placeholder":"Write your note here...",
                "required":False,
            })
        }

    def clean_text(self): 
        data = self.cleaned_data.get('text','')
        data = data.strip()

        if not data:
            raise forms.ValidationError("Cannot add empty Note")
        if len(data)<3:
            raise forms.ValidationError("Minimum 3 characters required.")
        if not re.search(r"[a-zA-Z0-9]", data):
            raise forms.ValidationError("Only Aplhanumerics allowed")
        
        return data
        
