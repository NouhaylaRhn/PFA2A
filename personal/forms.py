from django import forms
from .models import Fiche_de_condidature
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FicheForm(forms.ModelForm):
    class Meta:
        model = Fiche_de_condidature
        fields = ('nom', 'prenom', 'CIN', 'CNE' , 'Téléphone' , 'Lieu_de_naissance' , 'Date_de_naissance' , 'Adresse_physique' , 'Sexe' , 'Nationalité' , 'pdf')

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
