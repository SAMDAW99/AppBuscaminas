# Create your models here.
from django.db import models


class Tablero(models.Model):
    dimension_x = models.IntegerField()
    dimension_y = models.IntegerField()
    # Agrega otros campos necesarios para representar el tablero
