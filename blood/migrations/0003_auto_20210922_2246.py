# Generated by Django 3.2.5 on 2021-09-22 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0002_donation_accept'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
        migrations.RemoveField(
            model_name='donation',
            name='accept',
        ),
    ]