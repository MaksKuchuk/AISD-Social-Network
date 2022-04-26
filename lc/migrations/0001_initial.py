# Generated by Django 4.0.4 on 2022-04-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('status', models.TextField(blank=True)),
                ('education', models.TextField(blank=True)),
                ('foodpreferences', models.TextField(blank=True)),
                ('attitudetoalcohol', models.TextField(blank=True)),
                ('attitudetosmoking', models.TextField(blank=True)),
            ],
        ),
    ]
