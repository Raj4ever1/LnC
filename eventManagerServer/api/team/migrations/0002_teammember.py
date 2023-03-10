# Generated by Django 4.0.8 on 2023-01-20 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_user_role_userrolemap'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
                ('user_role_map_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userrolemap')),
            ],
        ),
    ]
