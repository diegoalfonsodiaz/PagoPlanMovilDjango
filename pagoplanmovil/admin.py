from django.contrib import admin
from pagoplanmovil.models import Cliente, Mes, MesAdmin, Pago, PagoAdmin, Factura

# Register your models here.
admin.site.register(Mes, MesAdmin)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Pago, PagoAdmin)
# Register your models here.
