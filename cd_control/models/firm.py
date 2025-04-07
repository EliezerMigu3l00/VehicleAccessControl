from django.db import models


class Firm(models.Model):
    name = models.CharField(max_length=255, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name