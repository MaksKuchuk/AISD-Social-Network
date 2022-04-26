# Generated by Django 4.0.4 on 2022-04-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginfrom', models.CharField(max_length=255)),
                ('loginto', models.CharField(max_length=255)),
                ('time', models.TimeField(auto_now_add=True)),
                ('message', models.TextField()),
            ],
        ),
    ]