# Generated by Django 4.0.5 on 2023-01-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0008_alter_programresource_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='google_form_check',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
