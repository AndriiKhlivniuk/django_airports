from django.contrib import admin
from .models import Airport
# Register your models here.



class AirportAdmin(admin.ModelAdmin):
    search_fields = ("name","ident")

admin.site.register(Airport, AirportAdmin)