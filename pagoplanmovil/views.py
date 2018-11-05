from django.shortcuts import render
#librería para manejar el envío de mensajes

from django.contrib import messages
from .forms import ClienteForm
from pagoplanmovil.models import Cliente, Mes, Pago, Factura
from django.shortcuts import redirect



# Create your views here.
def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            #post.published_date = timezone.now()
            post.save()
            return redirect('cliente_detail', pk=post.pk)
    else:
        form = ClienteForm()
    return render(request, 'pagoplanmovil/cliente_edit.html', {'form': form})
