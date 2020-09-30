from django.contrib import admin

# Register your models here.
from CrtlElect.snippers import Attr
from Lugares.models import Provincia, Ciudad


class CiudadInline(admin.StackedInline):
    model = Ciudad
    extra = 0

@admin.register(Provincia)
class Admin_Provincia(admin.ModelAdmin):
    list_display = Attr(Provincia)
    list_display_links = Attr(Provincia)
    inlines = [CiudadInline]

@admin.register(Ciudad)
class Admin_Ciudad(admin.ModelAdmin):
    list_display = Attr(Ciudad)
    list_display_links = Attr(Ciudad)