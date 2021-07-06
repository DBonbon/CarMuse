from django.contrib import admin
from .models import Cover

class CoverAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'pitch', 'image')

admin.site.register(Cover, CoverAdmin)