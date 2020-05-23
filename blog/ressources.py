from import_export import resources
from .models import fiche_de_condidature

class FicheResource(resources.ModelResource):
    class Meta:
        model = fiche_de_condidature
