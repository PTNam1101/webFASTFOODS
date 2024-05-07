from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
  list_display = ("customer","rating", "phonenum",)
  list_filter = ("rating",)
  search_fields = ("customer__username",)
  list_per_page = 20
  readonly_fields = ('id',)
  
admin.site.register(Profile, ProfileAdmin)