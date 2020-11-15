# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ruian(models.Model):
    kod_adm = models.BigIntegerField(blank=True, null=True)
    kod_obce = models.BigIntegerField(blank=True, null=True)
    nazev_obce = models.TextField(blank=True, null=True)
    kod_momc = models.TextField(blank=True, null=True)  # This field type is a guess.
    nazev_momc = models.TextField(blank=True, null=True)  # This field type is a guess.
    kod_mop = models.TextField(blank=True, null=True)  # This field type is a guess.
    nazev_mop = models.TextField(blank=True, null=True)  # This field type is a guess.
    kod_casti_obce = models.BigIntegerField(blank=True, null=True)
    nazev_casti_obce = models.TextField(blank=True, null=True)
    kod_ulice = models.TextField(blank=True, null=True)  # This field type is a guess.
    nazev_ulice = models.TextField(blank=True, null=True)
    typ_so = models.TextField(blank=True, null=True)
    cislo_domovni = models.BigIntegerField(blank=True, null=True)
    cislo_orientacni = models.TextField(blank=True, null=True)  # This field type is a guess.
    znak_cisla_orientacniho = models.TextField(blank=True, null=True)
    psc = models.BigIntegerField(blank=True, null=True)
    souradnice_y = models.TextField(blank=True, null=True)  # This field type is a guess.
    souradnice_x = models.TextField(blank=True, null=True)  # This field type is a guess.
    plati_od = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ruian'

