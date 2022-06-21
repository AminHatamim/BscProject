from django.db import models


class Project(models.Model):
    file_number = models.IntegerField("شماره پرونده" , primary_key=True)
    planning_permission=models.FileField("پروانه ساختمانی" , upload_to='files/')
    address=models.TextField("آدرس")
    area=models.DecimalField("متراژ",max_digits = 6, decimal_places = 2)
    lon=models.DecimalField("طول جغرافیایی",max_digits = 9, decimal_places = 6)
    lat=models.DecimalField("عرض جغرافیایی",max_digits = 9, decimal_places = 6)
    owner_name = models.CharField("نام مالک",max_length=50)
    owner_tel = models.CharField("شماره تلفن مالک",max_length=12)
    board_photo=models.ImageField("عکس تابلوی مشخصات" , upload_to='files/')
    mec_eng_name=models.CharField("نام ناظر مکانیک",max_length=50)
    mec_eng_tel=models.CharField("شماره تلفن ناظر مکانیک",max_length=12)
    elec_eng_name=models.CharField("نام ناظر برق",max_length=50)
    elec_eng_tel=models.CharField("شماره تلفن ناظر برق",max_length=12)
    civil_eng_name=models.CharField("نام ناظر عمران",max_length=50)
    civil_eng_tel=models.CharField("شماره تلفن ناظر عمران",max_length=12)
    arch_eng_name=models.CharField("نام ناظر معماری",max_length=50)
    arch_eng_tel=models.CharField("شماره تلفن ناظر معماری" ,max_length=12)
    arch_checklist=models.FileField("چک لیست معماری" , upload_to='files/')
    mec_checklist=models.FileField("چک لیست مکانیک" , upload_to='files/')
    elec_checklist=models.FileField("چک لیست برق" , upload_to='files/')
    civil_checklist=models.FileField("چک لیست عمران" , upload_to='files/')


    class Meta:
        verbose_name = "پرونده"
        verbose_name_plural = "پرونده ها"

class Visit(models.Model):
    project=models.ForeignKey(Project, on_delete = models.CASCADE)
    visit_number =models.IntegerField("شماره بازدید")
    visit_date = models.DateField("تاریخ بازدید")
    stage=models.CharField("مرحله ساختمانی" , max_length=50)
    visit_images=models.ImageField("تصاویر بازدید" , upload_to='files/')
    visit_notes=models.TextField("توضیحات بازدید")


    class Meta:
        verbose_name = "بازدید"
        verbose_name_plural = "بازدید ها"
