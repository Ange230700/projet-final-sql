# Generated by Django 4.1.5 on 2023-01-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_remove_employe_departement_id_alter_employe_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='type_contract',
            field=models.CharField(choices=[('OPTION_1', 'CDD'), ('OPTION_2', 'CDI'), ('OPTION_3', 'Autre')], default='CDD', max_length=100),
        ),
    ]
