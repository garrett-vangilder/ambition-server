# Generated by Django 2.0.4 on 2018-05-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='salary',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
