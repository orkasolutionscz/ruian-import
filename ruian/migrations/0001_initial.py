# Generated by Django 3.1.3 on 2020-11-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod_adm', models.BigIntegerField(blank=True, null=True)),
                ('kod_obce', models.BigIntegerField(blank=True, null=True)),
                ('nazev_obce', models.TextField(blank=True, null=True)),
                ('kod_momc', models.TextField(blank=True, null=True)),
                ('nazev_momc', models.TextField(blank=True, null=True)),
                ('kod_mop', models.TextField(blank=True, null=True)),
                ('nazev_mop', models.TextField(blank=True, null=True)),
                ('kod_casti_obce', models.BigIntegerField(blank=True, null=True)),
                ('nazev_casti_obce', models.TextField(blank=True, null=True)),
                ('kod_ulice', models.TextField(blank=True, null=True)),
                ('nazev_ulice', models.TextField(blank=True, null=True)),
                ('typ_so', models.TextField(blank=True, null=True)),
                ('cislo_domovni', models.BigIntegerField(blank=True, null=True)),
                ('cislo_orientacni', models.TextField(blank=True, null=True)),
                ('znak_cisla_orientacniho', models.TextField(blank=True, null=True)),
                ('psc', models.BigIntegerField(blank=True, null=True)),
                ('souradnice_y', models.TextField(blank=True, null=True)),
                ('souradnice_x', models.TextField(blank=True, null=True)),
                ('plati_od', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ruian',
            },
        ),
    ]
