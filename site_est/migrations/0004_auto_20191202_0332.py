# Generated by Django 2.2.6 on 2019-12-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_est', '0003_auto_20191202_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
