# Generated by Django 5.0.4 on 2024-05-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_tags'),
        ('tag', '0002_remove_tag_content_type_remove_tag_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, default='', to='tag.tag'),
        ),
    ]
