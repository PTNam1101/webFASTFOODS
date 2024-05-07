from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name",)
  search_fields = ("name",)
  readonly_fields = ('id',)
  
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
  list_display = ("name", "category", "price","ordered_times",)
  list_filter = ("price","category",)
  search_fields = ("name",)
  list_per_page = 20
  readonly_fields = ('id',)
  
admin.site.register(Product, ProductAdmin)

