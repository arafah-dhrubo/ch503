# Generated by Django 3.2.5 on 2021-10-07 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_post_thana'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blood.post'),
        ),
    ]
