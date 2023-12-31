# Generated by Django 4.2.5 on 2023-09-13 16:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='photos/company_logos')),
                ('company_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('country_image', models.ImageField(upload_to='photos/countries/')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('salary_min', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('salary_max', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('experience', models.CharField(max_length=255)),
                ('job_image', models.ImageField(blank=True, null=True, upload_to='photos/job_images/%Y/%m/%d')),
                ('job_description', models.TextField()),
                ('how_to_apply', models.TextField()),
                ('job_requirements', models.TextField()),
                ('skill', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('is_active', models.BooleanField(default=True)),
                ('job_type', models.CharField(choices=[('Onsite', 'Onsite'), ('Remote', 'Remote'), ('Hybryd', 'Hybryd')], default='Onsite', max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.company')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_positions', to='jobs.country')),
            ],
        ),
    ]
