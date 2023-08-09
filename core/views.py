from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Nota
from .forms import NotaForm



def create(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            print(new_form)
            new_form.autor = request.user
            new_form.save()
            return HttpResponse('<h3>Form salvo</h3>')
        return render(request, 'create.html', {'form':form})
        

    form = NotaForm()
    contexto = {'form':form}
    return render(request, 'create.html', contexto)


def list_notes(request):

    notas = Nota.objects.all()
    contexto = {'notas':notas}

    return render(request, 'list.html', contexto)


def delete_note(request, pk):
    nota = get_object_or_404(Nota, id=pk)
    nota.delete()
    return HttpResponse('Nota apagada!')
    
def update_note(request, pk):

    form_before_update = get_object_or_404(Nota, id=pk)

    if request.method == "POST":
        form = NotaForm(request.POST, instance=form_before_update)
        if form.is_valid():
            form.save()
            return redirect('/list/')
        

    form = NotaForm(instance=form_before_update)
    return render(request, 'update.html', {'form':form})
