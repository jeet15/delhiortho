# Generated by Django 3.0.8 on 2020-07-21 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_contactus_oldmember'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='lastname',
            new_name='email',
        ),
    ]
