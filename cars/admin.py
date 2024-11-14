from django.contrib import admin
from cars.models import Brand, Car


class BrandAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'create_at',)
    search_fields = ('name',)


    class Meta: 

        verbose_name = 'Brands'

admin.site.register(Brand, BrandAdmin)


class CarAdmin(admin.ModelAdmin):
   
    list_display = ('id', 'model', 'brand__name', 'color', 'factory_year', 'model_year', 'create_at',)
    search_fields = ('models',)
    list_filter = ('brand',)


    class Meta: 

        verbose_name = 'Cars'

admin.site.register(Car, CarAdmin)
