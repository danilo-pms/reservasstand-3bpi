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
    # Obter todas as reservas ordenadas por data
    reservas = Reserva.objects.all().order_by("data")
    
    # Verificar se o parâmetro de consulta 'nome' está presente na solicitação GET
    if request.GET.get('nome'):
        # Filtrar as reservas cujo nome contenha o valor fornecido em 'nome'
        reservas = reservas.filter(nome__icontains=request.GET.get('nome'))
    
    context = {'reservas': reservas}
    return render(request, "reservas/listar.html", context)


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