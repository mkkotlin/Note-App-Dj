from django import forms # type: ignore
from .models import Notes

class CreateNotes(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ("title","description","drop_down")

        # widgets = {
        #     'title': forms.TextInput( attrs={'class':'tt'})
        # }