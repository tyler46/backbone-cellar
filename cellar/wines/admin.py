from django.contrib import admin
from wines.models import Wine

class WineAdmin(admin.ModelAdmin):
    """Wine Admin."""
    pass

admin.site.register(Wine, WineAdmin)
