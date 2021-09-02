# Generated by Django 3.2.4 on 2021-06-15 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('count', models.IntegerField()),
                ('unit', models.CharField(max_length=120)),
                ('index', models.DecimalField(decimal_places=2, max_digits=11)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('empty', 'Empty')], max_length=10)),
                ('shipping', models.CharField(choices=[('paid', 'Paid'), ('free', 'Free'), ('self', 'Self')], max_length=10)),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]