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
        title = notes_form.cleaned_data['title']   #get specific field value
        new_title = notes_form.save(commit=False)  #prevent save
        # new_title.title = title.replace(' ','_').lower()  # modifing title
        new_title.save()                           # saving all field after modification
        notes_form = CreateNotes()
        return render(request,'Notes.html',{'saved':'saved',"notes_form": notes_form})
    

def view_saved(request):
    x = Notes.objects.all()
    return render(request,'ViewSaved.html',{'x':x,'Edit':True})





def get_by_id(request,id):
    print(id)
    x = get_list_or_404(Notes,id=id)
    return render(request,'ViewSaved.html',{'x':x})




def delete(request,id):
    ins = Notes.objects.filter(id=id)
    ins.delete()
    return redirect('saved')

def update(request,id):
    u = get_object_or_404(Notes,id=id)
    # u.title = u.title.replace('_',' ')
    # u.title = u.title.lower()  #capture data and modifying
    if request.method == 'POST':
        notes_form = CreateNotes(request.POST,instance=u)
        if notes_form.is_valid():
            notes_form.save()
            return redirect('saved')
    else:
        notes_form = CreateNotes(instance=u)
        # notes_form.fields['title'].widget.attrs['readonly'] = True  ##this is to set field editable/not
    return render(request,'update.html',{"notes_form": notes_form})
















# Earlier Used
# def get_by_title(request,slug):
#     slug = slugify(slug)
#     x = get_list_or_404(Notes, title=slug)
#     url = reverse('get_by_title',kwargs={'slug':slug})
#     return render(request,'ViewSaved.html',{'x':x,'url':url})

# def delete(request,slug):
#     slug = slugify(slug)
#     x = get_list_or_404(Notes, title=slug)
#     ins = Notes.objects.filter(title=slug)
#     ins.delete()
#     return redirect('saved')