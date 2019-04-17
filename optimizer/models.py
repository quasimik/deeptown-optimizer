from django.db import models

# Create your models here.
class Resource(models.Model):
	raw = models.BooleanField(default=False)
	value = models.IntegerField()

class Recipe(models.Model):
	product = models.ForeignKey(Resource, on_delete='PROTECT')
	ingredients = models.ManyToManyField(Resource, through='Ingredient', related_name='recipes')
	product_qty = models.IntegerField()
	time_sec = models.IntegerField()

class Ingredient(models.Model):
	resource = models.ForeignKey(Resource, on_delete='CASCADE')
	recipe = models.ForeignKey(Recipe, on_delete='CASCADE')
	qty = models.IntegerField()
