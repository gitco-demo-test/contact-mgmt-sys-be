# Generated by Django 4.2.4 on 2023-08-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
    ]