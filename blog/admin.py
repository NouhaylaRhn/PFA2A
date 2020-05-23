from django.contrib import admin
from .models import Fiche_de_condidature
from import_export import resources
from import_export.admin import ImportExportModelAdmin




@admin.register(Fiche_de_condidature)
class FicheAdmin(ImportExportModelAdmin):
    pass
'''


class FicheResource(resources.ModelResource):
	class Meta:
		model = Fiche_de_condidature '''

'''admin.site.register(Fiche_de_condidature) '''









'''
		

class MemberAdmin(ImportExportModelAdmin):
	resource_class = MemberResource



'''



