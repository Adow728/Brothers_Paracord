# Generated by Django 3.1.3 on 2020-11-12 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20201112_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcolor',
            name='item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='management.item'),
            preserve_default=False,
        ),
    ]
