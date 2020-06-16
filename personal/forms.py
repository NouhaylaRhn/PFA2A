from django import forms
from .models import Fiche_de_condidature, Recu, Carte
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FicheForm(forms.ModelForm):
    class Meta:
        model = Fiche_de_condidature
        fields = ('nom', 'prenom', 'CIN', 'CNE' , 'Téléphone' , 'Lieu_de_naissance' , 'Date_de_naissance' , 'Adresse_physique' , 'Sexe' , 'Nationalité' )

class CarteForm(forms.ModelForm):
    class Meta:
        model = Carte
        fields = ('nom', 'prenom', 'CIN' , 'Lieu_de_naissance' , 'Date_de_naissance' , 'Adresse_physique' , 'Sexe' , 'Nationalité' , 'pdf')



class RecuForm(forms.ModelForm):
    class Meta:
        model = Recu
        fields = ('Nom',  'Téléphone' , 'Email' , 'pdf')
        


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
