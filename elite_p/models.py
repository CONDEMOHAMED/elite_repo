from inspect import trace
from tabnanny import verbose
from django.db import models

# Create your models here.

class client(models.Model):
    num_client = models.IntegerField(primary_key=True,max_length=3)
    nom_client = models.CharField(max_length=50)
    adresse_client = models.CharField(max_length=50)
    telephone = models.CharField(max_length=18)
    class Meta:
          db_table = 'client'
          verbose_name = 'client'
          def __str__(self):
            return f"{self.type_client} {self.lib_type_client}"

class facture(models.Model):
    num_facture = models.IntegerField(primary_key=True,max_length=3)
    reffacture = models.IntegerField(primary_key=True,max_length=3)
    nom_client = models.CharField(max_length=50)
    date_facture = models.DateField(auto_now=trace)
   
    class Meta:
          db_table = 'facture'
          verbose_name = 'facture'
          def __str__(self):
            return f"{self.type_facture} {self.lib_type_facture}"

class periode(models.Model):
    num_periode = models.IntegerField(primary_key=True,max_length=3)
    date_debut = models.DateTimeField(null=True)
    date_fin = models.DateTimeField(null=True)
   
    class Meta:
          db_table = 'periode'
          verbose_name = 'periode'
          def __str__(self):
            return f"{self.type_periode} {self.lib_type_periode}"

class mode_reglement(models.Model):
    num_mode_reglement = models.IntegerField(primary_key=True,max_length=3)
    type_mode_reglement = models.DateTimeField(null=True)
    
    class Meta:
          db_table = 'mode_reglement'
          verbose_name = 'mode_reglement'
          def __str__(self):
            return f"{self.type_mode_reglement} {self.lib_type_mode_reglement}"

class article(models.Model):
    num_article = models.IntegerField(primary_key=True,max_length=3)
    date_recept_article = models.DateTimeField(null=True)
    
    class Meta:
          db_table = 'article'
          verbose_name = 'article'
          def __str__(self):
            return f"{self.type_article} {self.lib_type_article}"

class type_article(models.Model):
    num_type_article = models.IntegerField(primary_key=True,max_length=3)
    nom_type_article = models.CharField(max_length=50)
    class Meta:
          db_table = 'type_article'
          verbose_name = 'type_article'
          def __str__(self):
            return f"{self.type_article} {self.lib_type_article}"

class type_article_tarif(models.Model):
    num_type_article_tarif = models.IntegerField(primary_key=True,max_length=3)
    montant = models.DateTimeField(null=True)
    
    class Meta:
          db_table = 'type_article_tarif'
          verbose_name = 'type_article_tarif'
          def __str__(self):
            return f"{self.type_article_tarif} {self.lib_type_article_tarif}"







