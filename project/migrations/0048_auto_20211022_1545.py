# Generated by Django 3.2.7 on 2021-10-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0047_alter_issue_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='bonus_description',
            field=models.CharField(default='', max_length=200, verbose_name='Bonus Description'),
        ),
        migrations.AddField(
            model_name='issue',
            name='bonus_value',
            field=models.CharField(default='0', max_length=200, verbose_name='Bonus Value'),
        ),
    ]