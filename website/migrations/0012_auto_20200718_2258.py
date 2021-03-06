# Generated by Django 3.0.8 on 2020-07-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_newmember_paymentscreen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eposter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epostertitle', models.CharField(max_length=255)),
                ('posterfile', models.FileField(upload_to='eposter')),
            ],
        ),
        migrations.AlterField(
            model_name='members',
            name='paymenttype',
            field=models.CharField(choices=[('NEFT', 'NEFT'), ('Cheque ', 'select 2'), ('Cash Deposit', 'Cash Deposit')], max_length=200),
        ),
    ]
