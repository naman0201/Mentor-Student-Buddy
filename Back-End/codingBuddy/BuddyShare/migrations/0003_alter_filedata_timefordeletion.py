# Generated by Django 4.0.4 on 2022-09-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuddyShare', '0002_alter_filedata_timefordeletion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedata',
            name='TimeForDeletion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
