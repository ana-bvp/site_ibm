from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100) # Ex: Toyota, Honda
    description = models.TextField()
    def __str__(self): return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) # Ex: Corolla, Camry
    type = models.CharField(max_length=50, choices=[('Sedan','Sedan'),('SUV','SUV'),('Wagon','Wagon')])
    year = models.IntegerField(validators=[MaxValueValidator(2023), MinValueValidator(2015)]) #
    def __str__(self): return self.name
