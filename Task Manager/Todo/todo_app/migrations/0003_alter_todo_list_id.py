# Generated by Django 5.1.3 on 2024-12-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_todo_list_options_alter_todo_list_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
