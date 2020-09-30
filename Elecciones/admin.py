from django.contrib import admin

# Register your models here.
from CrtlElect.snippers import Attr
from Elecciones.models import *

@admin.register(PartidoPolitico)
class Admin_PartidoPolitico(admin.ModelAdmin):
    list_display_links = Attr(PartidoPolitico)
    list_display = Attr(PartidoPolitico)