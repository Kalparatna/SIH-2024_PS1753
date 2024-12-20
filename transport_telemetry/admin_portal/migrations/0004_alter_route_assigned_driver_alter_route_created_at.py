# Generated by Django 5.0.3 on 2024-09-28 06:39

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_portal', '0003_delete_gpslocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='assigned_driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_portal.driver'),
        ),
        migrations.AlterField(
            model_name='route',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
