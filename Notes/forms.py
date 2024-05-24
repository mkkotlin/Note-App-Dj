from django import forms
from .models import Notes

class CreateNotes(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ("title","description","drop_down")