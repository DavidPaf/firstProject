# Generated by Django 4.0.4 on 2022-04-18 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0002_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default=0, max_length=36, unique=True),
            preserve_default=False,
        ),
    ]
