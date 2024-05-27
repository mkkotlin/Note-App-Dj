from datetime import datetime
from django.shortcuts import render, get_list_or_404, redirect # type: ignore
from .forms import CreateNotes, Notes
from django.views.decorators.http import require_POST # type: ignore


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
    return render(request,'ViewSaved.html',{'x':x,'Edit':True})



def get_by_title(request,slug):
    x = get_list_or_404(Notes, title=slug)
    return render(request,'ViewSaved.html',{'x':x,})

def delete(request,slug):
    x = get_list_or_404(Notes, title=slug)
    ins = Notes.objects.filter(title=slug)
    print(ins)
    ins.delete()
    return redirect('saved')