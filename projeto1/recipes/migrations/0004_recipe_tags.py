# Generated by Django 5.0.4 on 2024-05-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_category_alter_recipe_cover_and_more'),
        ('tag', '0002_remove_tag_content_type_remove_tag_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='tag.tag'),
        ),
    ]
