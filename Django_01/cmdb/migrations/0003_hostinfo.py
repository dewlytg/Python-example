# Generated by Django 2.0 on 2017-12-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20171216_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.IntegerField(auto_created=1, primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=32)),
                ('status', models.CharField(max_length=16)),
                ('position', models.CharField(max_length=8)),
                ('venctor', models.CharField(max_length=32)),
                ('cputype', models.CharField(max_length=16)),
                ('memsize', models.CharField(max_length=32)),
                ('osname', models.CharField(max_length=16)),
            ],
        ),
    ]
