# Generated by Django 2.0 on 2017-12-17 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_hostinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='id',
            field=models.AutoField(max_length=16, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
    ]
