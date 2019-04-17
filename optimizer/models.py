from django.db import models

RAW_RPM = 6
RAW_T = 60 / RAW_RPM

# Create your models here.
class Resource(models.Model):
  name = models.CharField(max_length=50)
  raw = models.BooleanField(default=False)
  value = models.IntegerField()

  def __str__(this):
    return this.name

  def recipe(this):
    return this.recipe_set.first()

  def recipe_ingreds(this):
    return this.recipe().ingredient_set.all()

  def raw_value(this):
    if this.raw:
      return this.value
    val = 0
    for ing in this.recipe_ingreds():
      val += ing.qty * ing.resource.raw_value()
    val /= this.recipe().product_qty
    return val

  def profit(this):
    return this.value - this.raw_value()

  def time(this):
    if this.raw:
      return RAW_T
    time = this.recipe().time_sec
    for ing in this.recipe_ingreds():
      time += ing.qty * ing.resource.time()
    time /= this.recipe().product_qty
    return time

  def value_per_time(this):
    return this.value / this.time()

  def profit_per_time(this):
    return this.profit() / this.time()

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
