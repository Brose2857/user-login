# Generated by Django 4.0.4 on 2022-05-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginform', '0003_rename_name1_new_ticket_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_ticket',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='new_ticket',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
