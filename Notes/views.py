from datetime import datetime
from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404 # type: ignore
from .forms import CreateNotes, Notes
from django.views.decorators.http import require_POST # type: ignore
from django.urls import reverse
from django.utils.text import slugify


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
    slug = slugify(slug)
    x = get_list_or_404(Notes, title=slug)
    url = reverse('get_by_title',kwargs={'slug':slug})
    return render(request,'ViewSaved.html',{'x':x,'url':url})

def delete(request,slug):
    slug = slugify(slug)
    x = get_list_or_404(Notes, title=slug)
    ins = Notes.objects.filter(title=slug)
    print(ins)
    ins.delete()
    return redirect('saved')



def update(request,slug):
    slug = slugify(slug)
    u = get_object_or_404(Notes,title=slug)
    if request.method == 'POST':
        notes_form = CreateNotes(request.POST,instance=u)
        if notes_form.is_valid():
            notes_form.save()
            return redirect('saved')
    else:
        notes_form = CreateNotes(instance=u)
    return render(request,'update.html',{"notes_form": notes_form})


