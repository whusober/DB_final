# Generated by Django 3.0.6 on 2020-05-19 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20200518_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('未借出', '未借出'), ('已借出', '已借出'), ('续借', '续借')], default='未借出', max_length=11),
        ),
    ]
