# Generated by Django 4.2.3 on 2023-08-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogpost_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
