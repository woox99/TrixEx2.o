# Generated by Django 5.0.1 on 2024-01-13 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='booked_marked_users',
            field=models.ManyToManyField(related_name='bookmarks', to='app.user'),
        ),
    ]
