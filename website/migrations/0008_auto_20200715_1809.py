# Generated by Django 3.0.8 on 2020-07-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200715_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastmembers',
            name='annualmeet',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pastmembers',
            name='editor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pastmembers',
            name='president',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pastmembers',
            name='secretary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pastmembers',
            name='treasurer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
