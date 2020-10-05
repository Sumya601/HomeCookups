# Generated by Django 2.2 on 2020-10-02 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodManagement', '0007_food_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Food_Category',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Breakfast', max_length=50),
        ),
    ]