# Generated by Django 4.1.6 on 2023-02-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientid', models.IntegerField()),
                ('doctorid', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('type', models.CharField(max_length=80)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
