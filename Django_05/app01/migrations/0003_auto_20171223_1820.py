# Generated by Django 2.0 on 2017-12-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20171223_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(db_index=True, max_length=64)),
                ('ip', models.GenericIPAddressField(db_index=True)),
                ('port', models.IntegerField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='g',
            field=models.ForeignKey(on_delete=True, to='app01.HostGroup'),
        ),
    ]
