# Generated by Django 3.2.2 on 2021-06-02 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginAD', '0003_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='totals',
            field=models.IntegerField(null=True),
        ),
    ]
