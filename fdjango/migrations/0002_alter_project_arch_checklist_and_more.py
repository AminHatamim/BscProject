# Generated by Django 4.0.2 on 2022-06-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='arch_checklist',
            field=models.FileField(upload_to='files/', verbose_name='چک لیست معماری'),
        ),
        migrations.AlterField(
            model_name='project',
            name='board_photo',
            field=models.ImageField(upload_to='files/', verbose_name='عکس تابلوی مشخصات'),
        ),
        migrations.AlterField(
            model_name='project',
            name='civil_checklist',
            field=models.FileField(upload_to='files/', verbose_name='چک لیست عمران'),
        ),
        migrations.AlterField(
            model_name='project',
            name='elec_checklist',
            field=models.FileField(upload_to='files/', verbose_name='چک لیست برق'),
        ),
        migrations.AlterField(
            model_name='project',
            name='mec_checklist',
            field=models.FileField(upload_to='files/', verbose_name='چک لیست مکانیک'),
        ),
        migrations.AlterField(
            model_name='project',
            name='planning_permission',
            field=models.FileField(upload_to='files/', verbose_name='پروانه ساختمانی'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='visit_images',
            field=models.ImageField(upload_to='files/', verbose_name='تصاویر بازدید'),
        ),
    ]
