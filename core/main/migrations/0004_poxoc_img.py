# Generated by Django 5.1.3 on 2024-11-14 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_mayla_poxoc'),
    ]

    operations = [
        migrations.AddField(
            model_name='poxoc',
            name='img',
            field=models.ImageField(null=True, upload_to='poxoc', verbose_name='poxoci nkar'),
        ),
    ]
