# Generated by Django 4.1.5 on 2023-01-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('nombre_personne_departement', models.IntegerField()),
                ('date_de_creation_du_departement', models.DateField()),
                ('budget_annuel_du_departement', models.IntegerField()),
                ('responsable_departement', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Postes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=100)),
                ('Niveau_hiérarchique', models.CharField(max_length=100)),
                ('Salaire', models.IntegerField()),
                ('Département_id', models.IntegerField()),
                ('Statutposte', models.BooleanField()),
                ('type_contrat', models.IntegerField()),
            ],
        ),
    ]
