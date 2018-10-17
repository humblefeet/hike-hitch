# Generated by Django 2.1.1 on 2018-10-17 18:59

from django.db import migrations, models
import django.forms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20181017_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiker',
            name='experience',
            field=models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Experienced'), ('4', 'Advanced')], default='1', max_length=1, verbose_name=django.forms.fields.ChoiceField),
        ),
        migrations.AlterField(
            model_name='hiker',
            name='sex',
            field=models.CharField(choices=[('f', 'Female'), ('m', 'Male'), ('o', 'other')], max_length=1, verbose_name=django.forms.fields.ChoiceField),
        ),
        migrations.AlterField(
            model_name='trail',
            name='difficulty',
            field=models.CharField(choices=[('1', 'Easy'), ('2', 'Moderate'), ('3', 'Hard'), ('4', 'Advanced'), ('5', 'Extreme')], default='1', max_length=1, verbose_name=django.forms.fields.ChoiceField),
        ),
        migrations.AlterField(
            model_name='trip',
            name='difficulty',
            field=models.CharField(choices=[('1', 'Easy'), ('2', 'Moderate'), ('3', 'Hard'), ('4', 'Advanced'), ('5', 'Extreme')], default='1', max_length=1, verbose_name=django.forms.fields.ChoiceField),
        ),
    ]
