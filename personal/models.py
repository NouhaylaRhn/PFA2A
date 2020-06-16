from django.db import models

class Fiche_de_condidature (models.Model):
    nom = models.CharField(max_length = 140 , default='')
    prenom = models.CharField(max_length = 140 , default='')
    CIN = models.CharField(max_length = 140 , default='')
    CNE = models.CharField(max_length = 140 , default='')
    Téléphone = models.IntegerField(default='')
    Lieu_de_naissance = models.CharField(max_length = 140 , default='')
    Date_de_naissance = models.DateField()
    Adresse_physique = models.CharField(max_length = 140 , default='')
    Sexe = models.CharField(max_length = 140 , default='')
    Nationalité = models.CharField(max_length = 140 , default='')
    pdf = models.FileField(upload_to='fiches/pdfs/')
    
    

    def __str__(self):
        return self.nom



class Recu (models.Model):
    Nom = models.CharField(max_length = 140 , default='')
    Téléphone = models.IntegerField(default='')
    Adresse_physique = models.CharField(max_length = 140 , default='')
    Email = models.CharField(max_length = 140 , default='')
    pdf = models.FileField(upload_to='fiches/pdfs/')
    
    

    def __str__(self):
        return self.Nom


class Carte (models.Model):
    nom = models.CharField(max_length = 140 , default='')
    prenom = models.CharField(max_length = 140 , default='')
    CIN = models.CharField(max_length = 140 , default='')
    Lieu_de_naissance = models.CharField(max_length = 140 , default='')
    Date_de_naissance = models.DateField()
    Adresse_physique = models.CharField(max_length = 140 , default='')
    Sexe = models.CharField(max_length = 140 , default='')
    Nationalité = models.CharField(max_length = 140 , default='')
    pdf = models.FileField(upload_to='fiches/pdfs/')
    
    

    def __str__(self):
        return self.nom
