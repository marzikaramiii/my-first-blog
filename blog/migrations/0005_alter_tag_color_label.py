# Generated by Django 3.2.23 on 2024-01-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag_color_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color_label',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]