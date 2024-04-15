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

    def __str__(self):
        return self.User.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Banner(models.Model):
    title = models.CharField(max_length=55, verbose_name="sarlavha")
    description = models.CharField(max_length=255, verbose_name="tarif")
    image = models.ImageField(upload_to="banner_photo", verbose_name="rasm")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bosh sahifa'
        verbose_name_plural = 'Bosh sahifalar'


class Product(models.Model):
    name = models.CharField(max_length=35, verbose_name="nomi")
    description = models.CharField(max_length=75, verbose_name="tarif")
    retsept = models.TextField( verbose_name="tarif")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="naxri")
    tag = models.ForeignKey(to='Tag', on_delete=models.CASCADE, verbose_name="teg")
    image = models.ImageField(upload_to="product_photo", verbose_name="rasm")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Tag(models.Model):
    name = models.CharField(max_length=55, verbose_name="teg")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teg'
        verbose_name_plural = 'Teglar'


class Advantage(models.Model):
    title = models.CharField(max_length=55, verbose_name="sarlavfa")
    description = models.CharField(max_length=255, verbose_name="tarif")
    icon = models.ImageField(upload_to="advantage_icon", verbose_name="icon")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Afzallik'
        verbose_name_plural = 'Afzalliklar'


class Favorite_food(models.Model):
    description = models.CharField(max_length=255, verbose_name="tarif")
    icon = models.ImageField(upload_to="favorite_food/", verbose_name="icon")

    def __str__(self):
        return self.description


class Branch(models.Model):
    name = models.CharField(max_length=55, verbose_name="nomi")
    address = models.CharField(max_length=255, verbose_name="manzil")
    start_time = models.TimeField(verbose_name="boshlanish vaqt")
    end_time = models.TimeField(verbose_name="tugash vaqt")
    lat = models.FloatField()
    lot = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Filial'
        verbose_name_plural = 'Filiallar'


class Vacancy(models.Model):
    title = models.CharField(max_length=55, verbose_name="sarlavfa")
    text = models.TextField(verbose_name="to'liq malumot")
    description = models.CharField(max_length=75 , verbose_name="tarif")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ish haqida malomut'
        verbose_name_plural = 'Ishlar haqida malomut'


class Send_request(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="ism va falimiya")
    phone_number = models.CharField(max_length=13, verbose_name="telefon raqam")
    image = models.ImageField(upload_to="send_request_photo")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'


class Job_benefit(models.Model):
    title = models.CharField(max_length=35, verbose_name="sarlavha")
    text = models.TextField(verbose_name="toliq malomot")
    icon = models.ImageField(upload_to="job_benefit_icon/" , verbose_name="icon")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ish avfzalik'
        verbose_name_plural = 'ish avfzaliklari'


class Career(models.Model):
    fullname = models.CharField(max_length=75, verbose_name="ism familiya")
    bio = models.TextField(verbose_name="o'zi haqida malumot")
    image = models.ImageField(upload_to="career_photo/" , verbose_name="rasm")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'karyera'
        verbose_name_plural = 'karyeralar'


class About_job(models.Model):
    title = models.CharField(max_length=75, verbose_name="sarlavha")
    text = models.TextField(verbose_name="malumot")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ish malumot '
        verbose_name_plural = 'ish malumotlar'


class New(models.Model):
    title = models.CharField(max_length=75 , verbose_name="sarlavha")
    text = models.TextField(verbose_name="malumot")
    image = models.ImageField(upload_to="new_photo/", verbose_name="rasm")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'yangilik'
        verbose_name_plural = 'yangiliklar'


class About_us(models.Model):
    title = models.CharField(max_length=55, verbose_name="sarlavha")
    description = models.CharField(max_length=75, verbose_name="tarif")
    text = models.TextField(verbose_name="malumot")
    image = models.ImageField(upload_to="about_us/", verbose_name="rasm")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'biz haqimizda'
        verbose_name_plural = 'biz haqimizda'


class Resume(models.Model):
    title = models.CharField(max_length=55, verbose_name="saravha")
    text = models.TextField(verbose_name="malumot")
    image = models.ForeignKey(to="Image" , verbose_name="rasm tanlash" , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'rasm'
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

    def __str__(self):
        return self.fullame

    class Meta:
        verbose_name = 'izoh'
        verbose_name_plural = 'izohlar'


class Contact(models.Model):
    phone_number = models.CharField(max_length=13, verbose_name="telefon raqam")
    extra_number = models.CharField(max_length=13, verbose_name="yetgazib beruvchi telefon raqami")
    ofis_address = models.CharField(max_length=75, verbose_name="mazil ofis")

    def __str__(self):
        return self.ofis_address

    class Meta:
        verbose_name = 'kontak'
        verbose_name_plural = 'kontaklar'


class Info(models.Model):
    telegram = models.CharField(max_length=255, verbose_name="telegram")
    instagram = models.CharField(max_length=255, verbose_name="instagram")
    facebook = models.CharField(max_length=255, verbose_name="facebook")
    play_market = models.CharField(max_length=255, verbose_name="play_market")
    app_store = models.CharField(max_length=255, verbose_name="app_store")
    banner_logo = models.ImageField(upload_to="banner_logo/", verbose_name="banner_logo")
    banner_photo = models.ImageField(upload_to="banner_photo/", verbose_name="banner_photo")

    def __str__(self):
        return self.telegram

    class Meta:
        verbose_name = 'info'
        verbose_name_plural = 'infolar'

