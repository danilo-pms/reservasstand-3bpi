from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar")
    else:
        form = ReservaForm()
    context = {'form': form}
    return render(request, 'reservas/cadastro.html', context)

def listar(request):
    reservas = Reserva.objects.all()
    return render(request, "reservas/listar.html", {"reservas": reservas})

def excluir(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect("listar")

def atualizar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect("listar")
    else:
        form = ReservaForm(instance=reserva)
    
    context = {'form': form, 
               'reserva': reserva}
    return render(request, "reservas/cadastro.html", context)

def detalhes(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {'reserva': reserva}
    return render(request, "reservas/detalhes.html", context)