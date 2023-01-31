# Generated by Django 4.0.8 on 2023-01-24 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_user_role_userrolemap'),
        ('team', '0004_alter_participant_user_role_map_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='team_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.team'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='user_role_map_id',
            field=models.ForeignKey(blank=True, limit_choices_to={'role_id': 3}, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.userrolemap'),
        ),
    ]
