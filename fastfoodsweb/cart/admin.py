from django.contrib import admin
from .models import *

class CartAdmin(admin.ModelAdmin):
  list_display = ("customer","order", "product", "quantity","status")
  list_filter = ("status",)
  search_fields = ("customer__username", "order__id",)
  list_per_page = 20
  readonly_fields = ('id',)
  
admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
  list_display = ("customer","address", "orderedTime", "total","status")
  list_filter = ("total","status",)
  search_fields = ("customer__name","orderedTime")
  list_per_page = 20
  readonly_fields = ('id',)
  
admin.site.register(Order, OrderAdmin)

class AddressAdmin(admin.ModelAdmin):
  list_display = ("customer","address","default")
  
admin.site.register(Address,AddressAdmin)