# Generated by Django 4.0.6 on 2022-07-11 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userData', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ('username',)},
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='time_played',
            new_name='join_date',
        ),
    ]
