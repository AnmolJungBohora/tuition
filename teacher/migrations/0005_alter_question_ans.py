# Generated by Django 4.1.3 on 2023-01-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_alter_question_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ans',
            field=models.CharField(choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4')], default='', max_length=200),
        ),
    ]
