# Generated by Django 2.2 on 2020-09-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodManagement', '0005_food_merchant'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Food_Img',
            field=models.ImageField(default=1, upload_to='images/logo/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='Food_Desc',
            field=models.FileField(upload_to='files/constitution/'),
        ),
    ]
