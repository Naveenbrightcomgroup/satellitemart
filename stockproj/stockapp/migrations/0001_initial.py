# Generated by Django 4.1.7 on 2023-02-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('arriveddate', models.DateField()),
                ('productName', models.CharField(max_length=30)),
                ('productQ', models.CharField(max_length=30)),
                ('productP', models.FloatField()),
            ],
        ),
    ]
