# Generated by Django 3.2 on 2021-04-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=250)),
                ('image2', models.ImageField(upload_to='img')),
                ('description2', models.TextField(verbose_name='Empty')),
            ],
        ),
    ]