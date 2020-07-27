# Generated by Django 3.0.8 on 2020-07-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200715_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newmember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membertype', models.CharField(choices=[('lifetime', 'Lifetime Member'), ('associate', 'Associate Member')], max_length=200)),
                ('memberfees', models.IntegerField(null=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
    ]