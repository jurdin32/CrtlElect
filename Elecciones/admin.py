from django.contrib import admin

# Register your models here.
from CrtlElect.snippers import Attr
from Elecciones.models import PartidoPolitico


class Admin_PartidoPolitico(admin.ModelAdmin):
    list_filter = Attr(PartidoPolitico)
    list_display_links = Attr(PartidoPolitico)