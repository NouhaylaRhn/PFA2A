from django import forms

from .models import Fiche_de_condidature


class FicheForm(forms.ModelForm):
    class Meta:
        model = Fiche_de_condidature
        fields = ('nom', 'prenom', 'CIN', 'CNE' , 'Téléphone' , 'Lieu_de_naissance' , 'Date_de_naissance' , 'Adresse_physique' , 'Sexe' , 'Nationalité' , 'pdf')
