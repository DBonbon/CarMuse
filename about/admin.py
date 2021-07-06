from django.contrib import admin
from .models import AboutPage
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'link', 'contact_title', 'image')
admin.site.register(AboutPage, AboutPageAdmin)

