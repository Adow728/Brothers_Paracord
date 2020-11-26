# Generated by Django 3.1.3 on 2020-11-26 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20201126_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='builder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='management.employee'),
        ),
        migrations.AddField(
            model_name='order',
            name='sale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='management.sale'),
        ),
    ]
