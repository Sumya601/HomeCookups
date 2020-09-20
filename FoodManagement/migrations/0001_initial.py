# Generated by Django 2.2 on 2020-09-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Food_Name', models.CharField(max_length=200)),
                ('Food_Desc', models.CharField(max_length=200)),
                ('Food_Price', models.FloatField(max_length=200)),
            ],
        ),
    ]