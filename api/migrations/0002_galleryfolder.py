# Generated by Django 3.1.2 on 2020-10-11 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=10000)),
                ('image', models.ImageField(default='default_gallery.jpg', upload_to='gallery_section_pics/<django.db.models.fields.CharField>')),
                ('gallery', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.gallery')),
            ],
        ),
    ]