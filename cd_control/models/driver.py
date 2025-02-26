from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    cnh = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    firm = models.ForeignKey('Firm', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
