from django.contrib import admin
from .models import *

class items(admin.ModelAdmin):
    list_display = ['id','title', 'visible']

# Register your models here.
admin.site.register(Popularplace,items)
admin.site.register(Popularplace1,items)