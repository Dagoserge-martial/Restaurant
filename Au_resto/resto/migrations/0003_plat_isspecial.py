# Generated by Django 2.2.6 on 2019-10-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0002_auto_20191009_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='plat',
            name='isSpecial',
            field=models.BooleanField(default=False),
        ),
    ]
