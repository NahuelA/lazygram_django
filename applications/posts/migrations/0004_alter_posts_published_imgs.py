# Generated by Django 4.0.2 on 2022-06-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_posts_published_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='published_imgs',
            field=models.ImageField(null=True, upload_to='uploads/pictures_posted'),
        ),
    ]
