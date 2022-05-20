# Generated by Django 4.0.1 on 2022-02-14 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='base.property')),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.location'),
        ),
    ]
