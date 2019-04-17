from django.db import models

# Create your models here.
class Resource(models.Model):
  name = models.CharField(max_length=50)
  raw = models.BooleanField(default=False)
  value = models.IntegerField()

  def __str__(this):
    return this.name

class Recipe(models.Model):
  product = models.ForeignKey(Resource, on_delete='PROTECT')
  ingredients = models.ManyToManyField(Resource, through='Ingredient', related_name='recipes')
  product_qty = models.IntegerField()
  time_sec = models.IntegerField()

  def __str__(this):
    return this.product.name + ' (x' + str(this.product_qty) + ')'

  # def get_ingredients(self):
  #   return "\n".join([p.products for p in self.ingredients.all()])

class Ingredient(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete='CASCADE')
  resource = models.ForeignKey(Resource, on_delete='CASCADE')
  qty = models.IntegerField()

  def __str__(this):
    return this.resource.name + ' (x' + str(this.qty) + ') for ' + str(this.recipe)
