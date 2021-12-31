# Generated by Django 4.0 on 2021-12-21 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroomapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_details',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='news_details',
            name='img_url',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='news_details',
            name='source',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='news_details',
            name='title',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]