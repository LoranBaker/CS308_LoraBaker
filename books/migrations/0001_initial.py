# Generated by Django 2.2.10 on 2021-03-31 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=100)),
                ('authors', models.CharField(default='author', max_length=100)),
                ('publisher', models.CharField(default='publisher', max_length=100)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('number_of_pages', models.IntegerField(default=0)),
            ],
        ),
    ]
