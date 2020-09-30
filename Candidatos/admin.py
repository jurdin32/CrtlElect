from django.contrib import admin

# Register your models here.
from Candidatos.models import Dignidad
from CrtlElect.snippers import Attr

@admin.register(Dignidad)
class Admin_Dignidad(admin.ModelAdmin):
    list_display = Attr(Dignidad)
    list_display_links = Attr(Dignidad)