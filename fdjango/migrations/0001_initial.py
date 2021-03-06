# Generated by Django 4.0.2 on 2022-05-26 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('file_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='شماره پرونده')),
                ('planning_permission', models.FileField(upload_to='', verbose_name='پروانه ساختمانی')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('area', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='متراژ')),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='طول جغرافیایی')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='عرض جغرافیایی')),
                ('owner_name', models.CharField(max_length=50, verbose_name='نام مالک')),
                ('owner_tel', models.CharField(max_length=12, verbose_name='شماره تلفن مالک')),
                ('board_photo', models.ImageField(upload_to='', verbose_name='عکس تابلوی مشخصات')),
                ('mec_eng_name', models.CharField(max_length=50, verbose_name='نام ناظر مکانیک')),
                ('mec_eng_tel', models.CharField(max_length=12, verbose_name='شماره تلفن ناظر مکانیک')),
                ('elec_eng_name', models.CharField(max_length=50, verbose_name='نام ناظر برق')),
                ('elec_eng_tel', models.CharField(max_length=12, verbose_name='شماره تلفن ناظر برق')),
                ('civil_eng_name', models.CharField(max_length=50, verbose_name='نام ناظر عمران')),
                ('civil_eng_tel', models.CharField(max_length=12, verbose_name='شماره تلفن ناظر عمران')),
                ('arch_eng_name', models.CharField(max_length=50, verbose_name='نام ناظر معماری')),
                ('arch_eng_tel', models.CharField(max_length=12, verbose_name='شماره تلفن ناظر معماری')),
                ('arch_checklist', models.FileField(upload_to='', verbose_name='چک لیست معماری')),
                ('mec_checklist', models.FileField(upload_to='', verbose_name='چک لیست مکانیک')),
                ('elec_checklist', models.FileField(upload_to='', verbose_name='چک لیست برق')),
                ('civil_checklist', models.FileField(upload_to='', verbose_name='چک لیست عمران')),
            ],
            options={
                'verbose_name': 'پرونده',
                'verbose_name_plural': 'پرونده ها',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_number', models.IntegerField(verbose_name='شماره بازدید')),
                ('visit_date', models.DateField(verbose_name='تاریخ بازدید')),
                ('stage', models.CharField(max_length=50, verbose_name='مرحله ساختمانی')),
                ('visit_images', models.ImageField(upload_to='', verbose_name='تصاویر بازدید')),
                ('visit_notes', models.TextField(verbose_name='توضیحات بازدید')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdjango.project')),
            ],
            options={
                'verbose_name': 'بازدید',
                'verbose_name_plural': 'بازدید ها',
            },
        ),
    ]
