from django.contrib import admin

from django.contrib import admin
from .models import houses


class Houseadmin(admin.ModelAdmin):
    pass;


admin.site.register(houses, Houseadmin)
