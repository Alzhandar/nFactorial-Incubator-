# Generated by Django 5.0.4 on 2024-04-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hex_code', models.CharField(max_length=7)),
                ('hue', models.IntegerField()),
                ('saturation', models.IntegerField()),
                ('lightness', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Palette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('colors', models.ManyToManyField(to='palettes.color')),
            ],
        ),
    ]
