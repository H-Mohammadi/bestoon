# Generated by Django 3.0.8 on 2020-08-06 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200724_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passwordresetcodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=120)),
                ('time', models.DateTimeField()),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]