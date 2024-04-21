from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Banner(models.Model):
    title = models.CharField(max_length=55, verbose_name="sarlavha")
    description = models.CharField(max_length=255, verbose_name="tarif")
    image = models.ImageField(upload_to="banner_photo", verbose_name="rasm")

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Bosh sahifalar'


class Product(models.Model):
    name = models.CharField(max_length=35, verbose_name="nomi")
    description = models.CharField(max_length=75, verbose_name="tarif")
    retsept = models.TextField(verbose_name="tarif")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="naxri")
    tag = models.ForeignKey(to='Tag', on_delete=models.CASCADE, verbose_name="teg")
    image = models.ImageField(upload_to="product_photo", verbose_name="rasm")

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Maxsulotlar'


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Maxsulotlar'


class Tag(models.Model):
    name = models.CharField(max_length=55, verbose_name="name")

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Teglar'


class Advantage(models.Model):
    title = models.CharField(max_length=55, verbose_name="sarlavfa")
    description = models.CharField(max_length=255, verbose_name="tarif")
    icon = models.ImageField(upload_to="advantage_icon", verbose_name="icon")

    class Meta:
        verbose_name = 'Advantage'
        verbose_name_plural = 'Afzalliklar'


class Favorite_food(models.Model):
    description = models.CharField(max_length=255, verbose_name="tarif")
    icon = models.ImageField(upload_to="favorite_food/", verbose_name="icon")

    class Meta:
        verbose_name = 'Favorite_food'
        verbose_name_plural = 'Afzalliklar'



class Branch(models.Model):
    name = models.CharField(max_length=55, verbose_name="nomi")
    address = models.CharField(max_length=255, verbose_name="manzil")
    start_time = models.TimeField(verbose_name="boshlanish vaqt")
    end_time = models.TimeField(verbose_name="tugash vaqt")
    lat = models.FloatField()
    lot = models.FloatField()

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Filiallar'


class Vacancy(models.Model):
    title = models.CharField(max_length=55, verbose_name="sarlavfa")
    text = models.TextField(verbose_name="to'liq malumot")
    description = models.CharField(max_length=75 , verbose_name="tarif")

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Ishlar haqida malomut'


class Send_request(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="ism va falimiya")
    phone_number = models.CharField(max_length=13, verbose_name="telefon raqam")
    image = models.ImageField(upload_to="send_request_photo")

    class Meta:
        verbose_name = 'Send_request'
        verbose_name_plural = 'Arizalar'


class Job_benefit(models.Model):
    title = models.CharField(max_length=35, verbose_name="sarlavha")
    text = models.TextField(verbose_name="toliq malomot")
    icon = models.ImageField(upload_to="job_benefit_icon/" , verbose_name="icon")

    class Meta:
        verbose_name = 'Job_benefit'
        verbose_name_plural = 'ish avfzaliklari'


class Career(models.Model):
    fullname = models.CharField(max_length=75, verbose_name="ism familiya")
    bio = models.TextField(verbose_name="o'zi haqida malumot")
    image = models.ImageField(upload_to="career_photo/" , verbose_name="rasm")

    class Meta:
        verbose_name = 'Career'
        verbose_name_plural = 'karyeralar'


class About_job(models.Model):
    title = models.CharField(max_length=75, verbose_name="sarlavha")
    text = models.TextField(verbose_name="malumot")

    class Meta:
        verbose_name = 'About_job'
        verbose_name_plural = 'ish malumotlar'


class New(models.Model):
    title = models.CharField(max_length=75 , verbose_name="sarlavha")
    text = models.TextField(verbose_name="malumot")
    image = models.ImageField(upload_to="new_photo/", verbose_name="rasm")

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'yangiliklar'


class About_us(models.Model):
    title = models.CharField(max_length=55, verbose_name="sarlavha")
    description = models.CharField(max_length=75, verbose_name="tarif")
    text = models.TextField(verbose_name="malumot")
    image = models.ImageField(upload_to="about_us/", verbose_name="rasm")

    class Meta:
        verbose_name = 'About_us'
        verbose_name_plural = 'biz haqimizda'


class Resume(models.Model):
    title = models.CharField(max_length=55, verbose_name="saravha")
    text = models.TextField(verbose_name="malumot")
    image = models.ForeignKey(to="Image" , verbose_name="rasm tanlash" , on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'rasmlar'


class Image(models.Model):
    image = models.ImageField(upload_to="resume_photo/" , verbose_name="rasm")


class Testimonial(models.Model):
    full_name = models.CharField(max_length=55, verbose_name="ism familiya")
    comment = models.TextField(verbose_name="komentariya")
    TYPE_CHOICES = (
        ('telegram', 'telegram'),
        ('facebook', 'facebook'),
        ('instagram', 'instagram'),
    )
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'izohlar'


class Contact(models.Model):
    phone_number = models.CharField(max_length=13, verbose_name="telefon raqam")
    extra_number = models.CharField(max_length=13, verbose_name="yetgazib beruvchi telefon raqami")
    ofis_address = models.CharField(max_length=75, verbose_name="mazil ofis")

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'kontaklar'


class Info(models.Model):
    telegram = models.CharField(max_length=255, verbose_name="telegram")
    instagram = models.CharField(max_length=255, verbose_name="instagram")
    facebook = models.CharField(max_length=255, verbose_name="facebook")
    play_market = models.CharField(max_length=255, verbose_name="play_market")
    app_store = models.CharField(max_length=255, verbose_name="app_store")
    banner_logo = models.ImageField(upload_to="banner_logo/", verbose_name="banner_logo")
    banner_photo = models.ImageField(upload_to="banner_photo/", verbose_name="banner_photo")

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'info'



class Order(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    products = models.TextField()
    total = models.DecimalField(max_digits=20, decimal_places=2)




