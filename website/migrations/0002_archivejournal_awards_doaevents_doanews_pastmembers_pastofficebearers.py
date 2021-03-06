# Generated by Django 3.0.8 on 2020-07-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivejournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=250)),
                ('archivefile', models.FileField(upload_to='archivejournal')),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('person', models.CharField(max_length=250)),
                ('year', models.IntegerField(null=True)),
                ('awardfile', models.FileField(upload_to='awards')),
            ],
        ),
        migrations.CreateModel(
            name='Doaevents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(default='upcoming', max_length=150)),
                ('edate', models.IntegerField(null=True)),
                ('emonth', models.IntegerField(null=True)),
                ('eyear', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=250)),
                ('efile', models.FileField(null=True, upload_to='eventfile')),
            ],
        ),
        migrations.CreateModel(
            name='Doanews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=250)),
                ('newsfile', models.FileField(upload_to='doanews')),
            ],
        ),
        migrations.CreateModel(
            name='Pastmembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('president', models.CharField(max_length=200)),
                ('secretary', models.CharField(max_length=200)),
                ('treasurer', models.CharField(max_length=200)),
                ('editor', models.CharField(max_length=200)),
                ('annualmeet', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pastofficebearers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.IntegerField(null=True)),
                ('designation', models.CharField(max_length=250)),
                ('image', models.FileField(upload_to='pastmembers')),
            ],
        ),
    ]
