# Generated by Django 3.0.8 on 2020-07-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_members_memberid'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
