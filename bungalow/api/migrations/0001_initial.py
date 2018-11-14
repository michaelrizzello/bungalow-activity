# Generated by Django 2.1.3 on 2018-11-14 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(max_length=10)),
                ('bathrooms', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('last_sold_date', models.DateField()),
                ('last_sold_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property_size', models.IntegerField()),
                ('tax_value', models.IntegerField()),
                ('tax_year', models.IntegerField()),
                ('year_built', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RentalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rentzestimate_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rentzestimate_last_updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ZillowDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zestimate_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('zestimate_last_updated', models.DateField()),
                ('zillow_id', models.IntegerField()),
                ('link', models.CharField(max_length=255)),
            ],
        ),
    ]