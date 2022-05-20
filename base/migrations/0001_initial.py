# Generated by Django 4.0.1 on 2022-02-14 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('companyname', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone1', models.CharField(max_length=20)),
                ('phome2', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=300)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=200)),
                ('clients', models.CharField(max_length=10)),
                ('rented', models.CharField(max_length=10)),
                ('sales', models.CharField(max_length=15)),
                ('sellingDescription', models.TextField(max_length=300)),
                ('leasingDescription', models.TextField(max_length=300)),
                ('advertisingDescription', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('companyname', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('area', models.DecimalField(decimal_places=2, max_digits=9)),
                ('bedroom', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('usage', models.CharField(choices=[('Rent', 'Rent'), ('Sell', 'Sell')], max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.owners')),
            ],
        ),
        migrations.CreateModel(
            name='ClientMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('comments', models.TextField(max_length=500)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.property')),
            ],
        ),
    ]
