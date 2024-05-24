from django.shortcuts import render
from .forms import CreateNotes


# Create your views here.


def home(request):
    notes_form = CreateNotes(request.POST or None)
    return render(request,'Notes.html',{"notes_form": notes_form})

def save(request):
    notes_form = CreateNotes(request.POST or None)
    if notes_form.is_valid():
        notes_form.save()
        notes_form = CreateNotes()
        return render(request,'Notes.html',{'saved':'saved',"notes_form": notes_form})