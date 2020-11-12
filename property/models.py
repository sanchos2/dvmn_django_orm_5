from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Claim(models.Model):
    """Модель жалобы."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто жаловался')
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, verbose_name='Квартира на которую пожаловались')
    text = models.TextField('Текст жалобы')

    def __str__(self):
        """Вывод в админку."""
        return f'{self.owner} {self.flat}'


class Flat(models.Model):
    """Модель квартиры."""

    new_building = models.NullBooleanField('Новостройка', db_index=True)
    created_at = models.DateTimeField('Когда создано объявление', default=timezone.now, db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField('Город, где находится квартира', max_length=50, db_index=True)  # noqa: WPS432
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,  # noqa: WPS432
        blank=True,
        help_text='Чертаново Южное',
    )
    address = models.TextField('Адрес квартиры', help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField('Этаж', max_length=3, help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField('Количество комнат в квартире', db_index=True)
    living_area = models.IntegerField('количество жилых кв.метров', null=True, blank=True, db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField('Год постройки здания', null=True, blank=True, db_index=True)
    like = models.ManyToManyField(User, symmetrical=False, blank=True, verbose_name='Кто лайкнул')

    def __str__(self):
        """Вывод в админку."""
        return f'{self.town}, {self.address} ({self.price}р.)'


class Owner(models.Model):
    """Модель собственников кваритры."""

    owner = models.CharField('ФИО владельца', max_length=200, db_index=True)  # noqa: WPS432
    owner_pure_phone = PhoneNumberField('Нормализованный номер владельца', blank=True, db_index=True)
    flat_owner = models.ManyToManyField('Flat', related_name='owners')

    def __str__(self):
        """Вывод в админку."""
        return self.owner
