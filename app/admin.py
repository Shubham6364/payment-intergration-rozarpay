from django.contrib import admin
from .models import *
# Register your models here.


class CofeeAdmin(admin.ModelAdmin):
    fields = ['name','amount','payment_id','paid']


admin.site.register(Cofee, CofeeAdmin)
