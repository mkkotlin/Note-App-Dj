from django.shortcuts import render, get_object_or_404
from .forms import CreateNotes, Notes
from django.views.decorators.http import require_POST


# Create your views here.


def home(request):
    notes_form = CreateNotes(request.POST or None)
    return render(request,'Notes.html',{"notes_form": notes_form})

@require_POST
def save(request):
    notes_form = CreateNotes(request.POST or None)
    if notes_form.is_valid():
        notes_form.save()
        notes_form = CreateNotes()
        return render(request,'Notes.html',{'saved':'saved',"notes_form": notes_form})
    

def view_saved(request):
    x = Notes.objects.all()
    print(x)
    return render(request,'ViewSaved.html',{'x':x})



def get_by_title(request,slug):
    x = get_object_or_404(Notes, title=slug)
    return render(request,'ViewSaved.html',{'x':x})