# Generated by Django 2.0.4 on 2018-05-10 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='first_player',
        ),
        migrations.RemoveField(
            model_name='game',
            name='next_to_move',
        ),
        migrations.RemoveField(
            model_name='game',
            name='second_player',
        ),
        migrations.RemoveField(
            model_name='move',
            name='game',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Move',
        ),
    ]
