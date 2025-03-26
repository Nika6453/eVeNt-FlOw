from django.db import models
from pytils.translit import slugify

class Category(models.Model):
    name = models.CharField("Название категории", max_length=30)
    slug=models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class PrivateCat(models.Model):
    name = models.CharField("Название категории", max_length=30)
    slug=models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name="Приватная категория"
        verbose_name_plural="Приватные категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Public(models.Model):
    title = models.CharField('Название мероприятия', max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    name = models.CharField('Введите ваше имя', max_length=30)
    price = models.CharField('Цена мероприятия', max_length=30)
    discription =  models.TextField('Описание')
    adress =  models.CharField('адресс', max_length=80)
    date = models.DateField()
    phone = models.CharField("Номер для связи", max_length=14)
    image = models.ImageField("Картинка мероприятия", upload_to="event_images/", blank=True, null=True)

    class Meta:
        verbose_name="Мероприятие"
        verbose_name_plural="Мероприятия"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Private(models.Model):
    title = models.CharField('Название мероприятия', max_length=30)
    category = models.ForeignKey(PrivateCat, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    name = models.CharField('Введите ваше имя', max_length=30)
    price = models.CharField('Цена мероприятия', max_length=30)
    discription =  models.TextField('Описание')
    adress =  models.CharField('адресс', max_length=80)
    date = models.DateField()
    phone = models.CharField("Номер для связи", max_length=14)
    image = models.ImageField("Картинка мероприятия", upload_to="event_images/", blank=True, null=True)

    class Meta:
        verbose_name="Частное Мероприятие"
        verbose_name_plural="Частные Мероприятия"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)