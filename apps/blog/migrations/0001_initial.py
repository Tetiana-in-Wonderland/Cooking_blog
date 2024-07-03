# Generated by Django 4.2.11 on 2024-07-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads')),
                ('ingredients', models.TextField()),
                ('utensils', models.TextField()),
                ('nutrutionperserving', models.TextField()),
                ('preparationsteps', models.TextField()),
            ],
        ),
    ]
