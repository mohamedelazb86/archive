from django.contrib import admin

from .models import Sectors,Documents

class DocumentAdmin(admin.ModelAdmin):
    list_display=['name',]
    search_fields=['name','notes']

class SectorAdmin(admin.ModelAdmin):
    list_display=['name','code']
    search_fields=['name']

admin.site.register(Sectors,SectorAdmin)
admin.site.register(Documents,DocumentAdmin)