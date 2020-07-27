# Generated by Django 3.0.8 on 2020-07-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20200721_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='certificatecreen',
        ),
        migrations.AddField(
            model_name='members',
            name='certificatescreen',
            field=models.FileField(blank=True, null=True, upload_to='members'),
        ),
        migrations.AddField(
            model_name='members',
            name='member_image',
            field=models.FileField(blank=True, null=True, upload_to='members'),
        ),
        migrations.AddField(
            model_name='members',
            name='password',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='members',
            name='clinicaddress',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='contactno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='degreescreen',
            field=models.FileField(blank=True, null=True, upload_to='members'),
        ),
        migrations.AlterField(
            model_name='members',
            name='extrainterest',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='hospital',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='institute',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='interest',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='peraddress',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='postaddress',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='state',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='study',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
    ]
