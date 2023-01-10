# Generated by Django 4.0.5 on 2023-01-02 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0007_programresource_document_upload_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programresource',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.program', verbose_name='Program'),
        ),
    ]