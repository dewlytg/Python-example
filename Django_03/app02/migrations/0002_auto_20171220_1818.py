# Generated by Django 2.0 on 2017-12-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='code',
            field=models.CharField(default='OP', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='host',
            name='port',
            field=models.IntegerField(),
        ),
    ]