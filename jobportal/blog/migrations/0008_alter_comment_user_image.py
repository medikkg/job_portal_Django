# Generated by Django 4.2.5 on 2023-09-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_image',
            field=models.ImageField(blank=True, default='photos/comments/userdef.jpg', null=True, upload_to='photos/comments/'),
        ),
    ]
