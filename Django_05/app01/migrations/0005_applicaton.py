# Generated by Django 2.0 on 2017-12-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20171225_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicaton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('h', models.ManyToManyField(to='app01.Host')),
            ],
        ),
    ]
