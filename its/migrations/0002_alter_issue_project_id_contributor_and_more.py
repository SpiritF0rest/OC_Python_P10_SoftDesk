# Generated by Django 4.2.2 on 2023-06-14 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('its', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='its.project'),
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('RO', 'droit de lecture seulement'), ('RW', 'droit de lecture et écriture')], default=None, max_length=2)),
                ('role', models.CharField(choices=[('AU', 'auteur'), ('CO', 'contributeur')], max_length=2)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='its.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
