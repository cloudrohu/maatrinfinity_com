# Generated by Django 5.0.2 on 2025-03-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_amenities_icone2_amenities_title2'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='site_ddress',
            field=models.CharField(blank=True, max_length=1150, null=True),
        ),
    ]
