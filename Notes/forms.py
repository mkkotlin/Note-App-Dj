from django import forms # type: ignore
from .models import Notes

class CreateNotes(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ("title","description","drop_down")
        
        widgets = {
            'title': forms.TextInput( attrs={'class':'form-control ','class':'container-fluid'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'drop_down': forms.Select(attrs={'class':'form-control'}),
        }