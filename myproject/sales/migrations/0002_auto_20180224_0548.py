# Generated by Django 2.0.2 on 2018-02-24 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user_name',
            new_name='user',
        ),
    ]
