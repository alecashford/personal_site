# Generated by Django 2.1.7 on 2019-03-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190315_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='intro',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
