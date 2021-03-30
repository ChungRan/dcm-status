# Generated by Django 3.1.7 on 2021-03-30 15:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawledDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.TextField()),
                ('gall_id', models.TextField()),
                ('comparedToPreviousday', models.IntegerField(null=True)),
                ('date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crawling.crawleddate')),
            ],
        ),
    ]
