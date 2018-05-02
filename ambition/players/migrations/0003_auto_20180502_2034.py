# Generated by Django 2.0.4 on 2018-05-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20180502_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='player',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
