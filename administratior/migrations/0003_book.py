# Generated by Django 4.1.3 on 2023-01-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administratior', '0002_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=1000)),
                ('pdf', models.FileField(upload_to='bookapp/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='bookapp/covers/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
