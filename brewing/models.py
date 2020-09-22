from django.db import models
from django.utils import timezone


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Charge(models.Model):
    production = models.DateTimeField()
    amount = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.production)


class BeerStorage(models.Model):
    keg_nr = models.AutoField(primary_key=True)
    volume = models.IntegerField()
    content = models.ForeignKey(Charge, on_delete=models.CASCADE, blank=True, null=True)
    filling = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, default='empty')

    def __str__(self):
        return "[" + str(self.keg_nr) + "] " + str(self.content)


class Fermentation(models.Model):
    charge = models.ForeignKey(Charge, on_delete=models.CASCADE)
    temperature = models.FloatField()
    fermentation = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return "[" + str(self.charge) + "] "


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return "[" + str(self.recipe) + "] " + str(self.step) + ". " + str(self.title)


class IngredientStorage(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    amount = models.FloatField()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.FloatField()
    ingredients = models.ForeignKey(IngredientStorage, on_delete=models.CASCADE)

    def __str__(self):
        return "[" + str(self.recipe) + "] " + str(self.ingredients)