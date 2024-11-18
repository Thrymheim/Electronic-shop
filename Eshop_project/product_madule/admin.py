from django.contrib import admin
from . import models

class productAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title', 'price','rating','is_active', 'category']
    list_filter = ['price','rating','is_active']
    list_editable = ['price','rating','is_active']
admin.site.register(models.product, productAdmin )
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductInformation)
admin.site.register(models.ProductTags)
