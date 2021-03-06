# Generated by Django 3.2.5 on 2021-07-26 11:13

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.TextField()),
                ('file', easy_thumbnails.fields.ThumbnailerImageField(upload_to='products')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
