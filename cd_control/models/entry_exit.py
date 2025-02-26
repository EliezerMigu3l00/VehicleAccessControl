from django.db import models


class EntryExit(models.Model):
    ENTRY_TYPES = [
        ('materia_prima', 'Recebimento de Matéria-Prima'),
        ('carregamento', 'Carregamento'),
        ('residuos', 'Retirada de Resíduos'),
        ('leite', 'Entrada de Leite'),
        ('visitantes', 'Entrada de Visitantes/Terceiros'),
    ]

    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    firm = models.ForeignKey('Firm', on_delete=models.CASCADE)
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPES)
    entry_datetime = models.DateTimeField(auto_now_add=True)
    start_unload_datetime = models.DateTimeField(blank=True, null=True)
    end_unload_datetime = models.DateTimeField(blank=True, null=True)
    exit_datetime = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    product_type = models.ForeignKey('ProductType', on_delete=models.SET_NULL, blank=True, null=True)
    pallets_quantity = models.IntegerField(blank=True, null=True)
    origin_route = models.CharField(max_length=255, blank=True, null=True)
    authorized_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.vehicle.vehicle_plate} - {self.entry_datetime}"
