# Generated by Django 4.0.1 on 2022-05-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_features_property_property_amenities_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owners',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.AddField(
            model_name='owners',
            name='phone2',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
