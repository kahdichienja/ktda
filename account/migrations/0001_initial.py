# Generated by Django 2.1.7 on 2021-03-23 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=191)),
                ('id_number', models.IntegerField()),
                ('ktda_number', models.CharField(max_length=191, unique=True)),
                ('profile', models.FileField(upload_to='userprofile')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_kilo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tea_type', models.CharField(choices=[('PT', 'Purple Tea'), ('BT', 'Black Tea'), ('DT', 'Dark Tea'), ('WT', 'White Tea')], max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('admin_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.FarmerModel')),
            ],
        ),
    ]
