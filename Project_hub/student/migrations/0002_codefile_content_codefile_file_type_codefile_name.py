# Generated by Django 5.1.1 on 2024-10-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codefile',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='codefile',
            name='file_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='codefile',
            name='name',
            field=models.CharField(default='txt', max_length=255),
            preserve_default=False,
        ),
    ]
