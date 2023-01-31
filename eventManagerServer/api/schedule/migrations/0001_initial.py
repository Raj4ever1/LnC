# Generated by Django 4.0.8 on 2023-01-20 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('match', '0001_initial'),
        ('event', '0005_eventusermap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('round', models.IntegerField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.match')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.room')),
            ],
        ),
        migrations.CreateModel(
            name='EventScheduleMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventgamemap')),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.schedule')),
            ],
        ),
    ]
