# Generated by Django 4.0.8 on 2023-01-20 09:01

import api.utills.constraints
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_rule'),
        ('event', '0003_alter_event_max_players_alter_event_min_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventGameMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('not_started', 'NOT_STARTED'), ('on_going', 'ON_GOING'), ('completed', 'COMPLETED'), ('canceled', 'CANCELED')], default=api.utills.constraints.TransactionStatus['NOT_STARTED'], max_length=20)),
                ('max_players', models.IntegerField(default=0)),
                ('min_players', models.IntegerField(default=0)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]
