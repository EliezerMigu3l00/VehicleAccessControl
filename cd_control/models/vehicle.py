from django.db import models


class Vehicle(models.Model):
    vehicle_plate = models.CharField(max_length=7, unique=True)
    cart_plate = models.CharField(max_length=7, unique=True, blank=True, null=True)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE)
    firm = models.ForeignKey('Firm', on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_plate
