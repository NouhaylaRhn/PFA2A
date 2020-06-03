from django.contrib import admin
from .models import Fiche_de_condidature
from import_export import resources
from import_export.admin import ImportExportModelAdmin




@admin.register(Fiche_de_condidature)
class FicheAdmin(ImportExportModelAdmin):
    pass




