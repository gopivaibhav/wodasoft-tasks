# Generated by Django 4.1.3 on 2022-12-08 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.RemoveField(
            model_name='article',
            name='checking_name',
        ),
    ]
