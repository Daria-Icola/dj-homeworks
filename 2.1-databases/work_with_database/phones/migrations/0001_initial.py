# Generated by Django 4.2.4 on 2023-09-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]
