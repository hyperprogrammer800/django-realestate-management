# Generated by Django 4.2.7 on 2023-12-07 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')], max_length=4)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.property')),
            ],
        ),
        migrations.CreateModel(
            name='RentalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('rent_date', models.PositiveIntegerField()),
                ('tenant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.unit')),
            ],
        ),
    ]