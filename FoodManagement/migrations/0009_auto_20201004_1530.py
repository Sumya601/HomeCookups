# Generated by Django 2.2 on 2020-10-04 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FoodManagement', '0008_food_food_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Food_Image',
            field=models.ImageField(blank=True, default='Foods/images/default.jpg', upload_to='Foods/images/'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='4', max_length=10)),
                ('comment', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='reviews',
            field=models.ManyToManyField(to='FoodManagement.Review'),
        ),
    ]
