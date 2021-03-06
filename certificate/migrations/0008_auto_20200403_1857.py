# Generated by Django 3.0.4 on 2020-04-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0007_auto_20200403_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='org',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
