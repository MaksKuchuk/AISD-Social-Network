# Generated by Django 4.0.4 on 2022-04-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lc', '0002_alter_lc_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login1', models.CharField(max_length=255)),
                ('login2', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequestList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginfrom', models.CharField(max_length=255)),
                ('loginto', models.CharField(max_length=255)),
            ],
        ),
    ]
