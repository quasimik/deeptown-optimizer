from django.contrib import admin
from .models import *

# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
	list_display = ['name', 'raw', 'value']

class RecipeAdmin(admin.ModelAdmin):
	list_display = ['product', 'product_qty', 'time_sec']
	# list_display = ['product', 'ingredients', 'product_qty', 'time_sec']

admin.site.register(Resource, ResourceAdmin)
# admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Recipe)
admin.site.register(Ingredient)
