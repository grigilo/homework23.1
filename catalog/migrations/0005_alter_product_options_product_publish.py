# Generated by Django 4.2.2 on 2024-06-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_edit_description', 'Can edit description'), ('can_edit_category', 'Can edit category'), ('can_cancel_publish', 'Can cancel publish')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='опубликован'),
        ),
    ]