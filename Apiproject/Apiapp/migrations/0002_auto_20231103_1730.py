# Generated by Django 3.2.23 on 2023-11-03 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient_records',
            options={'verbose_name_plural': 'Patient_Records'},
        ),
        migrations.RemoveField(
            model_name='patient_records',
            name='Department',
        ),
        migrations.AddField(
            model_name='patient_records',
            name='Doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor_records', to=settings.AUTH_USER_MODEL, verbose_name='Doctor'),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patient_records',
            name='Patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_records', to=settings.AUTH_USER_MODEL, verbose_name='patient'),
        ),
        migrations.AlterField(
            model_name='patient_records',
            name='Record_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient_records',
            name='idMisc',
            field=models.TextField(default='', verbose_name='Miscellaneous'),
        ),
    ]