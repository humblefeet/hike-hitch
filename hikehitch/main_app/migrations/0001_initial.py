# Generated by Django 2.1.1 on 2018-10-13 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('difficulty', models.CharField(choices=[('1', 'Easy'), ('2', 'Moderate'), ('3', 'Hard'), ('4', 'Advanced'), ('5', 'Extreme')], default='1', max_length=1)),
            ],
        ),
    ]
