# Generated by Django 2.2.1 on 2019-05-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='job_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
    ]