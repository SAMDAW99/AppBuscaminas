from django.shortcuts import render

from .forms import TableroForm

from .logicabuscaminas import Tablero

def welcome(request):
    return render(request, 'buscaminas1/index.html', {})


def crea_tablero(request):
    form = TableroForm()
    tablero = None
    show_alert = False
    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            columnas = form.cleaned_data['columnas']
            filas = form.cleaned_data['filas']
            minas = form.cleaned_data['minas']
            if minas<= filas*columnas/2:
                tablero = Tablero(filas, columnas, minas)
                tablero.contar_minas_adyacentes()
                return render(request, 'buscaminas1/mostrar_tablero.html', {'tablero': tablero})
            else:
                show_alert = True
    return render(request, 'buscaminas1/crea_tablero.html', {'form': form, 'show_alert': show_alert})
