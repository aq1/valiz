# coding=utf-8

from django.db import models


class Doctor(models.Model):

    TYPE = (
        (0, u'УЗИ'),
        (1, u'Функциональная диагностика'),
        (2, u'Консультация врача кардиолога'),
    )
    CATEGORY = (
        (0, u'Высшая'),
        (1, u'Первая'),
        (2, u'Вторая'),
    )
    type = models.IntegerField(choices=TYPE, default=0, verbose_name=u'Тип')
    category = models.IntegerField(choices=CATEGORY, default=0, verbose_name=u'Категория')
    short_title = models.CharField(max_length=255, blank=True, default=u'', verbose_name=u'Короткое описание')
    name = models.CharField(max_length=255, verbose_name=u'ФИО')
    bio = models.TextField(verbose_name=u'Биография', blank=True, default=u'')

    class Meta:
        verbose_name = u'Врач'
        verbose_name_plural = u'Врачи'
        ordering = ['type', 'name']

    def schedule(self):
        return Schedule.objects.filter(doctor=self)

    def biography(self):
        return self.bio.splitlines()

    def short_name(self):
        try:
            return u'{} {[0]}. {[0]}.'.format(*self.name.split())
        except IndexError:
            return self.name

    def __unicode__(self):
        return self.short_name()


class Schedule(models.Model):

    DAYS = (
        (0, u'Понедельник'),
        (1, u'Вторник'),
        (2, u'Среда'),
        (3, u'Четверг'),
        (4, u'Пятница'),
        (5, u'Суббота'),
        (6, u'Воскресенье'),
    )
    PARITY = (
        (0, u'Всегда'),
        (1, u'Нечет'),
        (2, u'Чет'),
    )

    doctor = models.ForeignKey(Doctor, verbose_name=u'Доктор')
    day = models.IntegerField(choices=DAYS, verbose_name=u'День')
    parity = models.IntegerField(choices=PARITY, verbose_name=u'Четный\Нечетный', blank=True, default=0)
    begin = models.TimeField(verbose_name=u'Начало')
    end = models.TimeField(verbose_name=u'Конец')

    class Meta:
        verbose_name = u'Расписание врача'
        verbose_name_plural = u'Расписания врача'
        ordering = ['day', 'parity']

    def __unicode__(self):
        return u'{} {} {} - {}'.format(
            self.DAYS[self.day][1],
            self.PARITY[self.parity][1],
            self.begin,
            self.end,
        )


class PriceList(models.Model):

    name = models.CharField(max_length=255, verbose_name=u'Название')

    class Meta:
        verbose_name = u'Прайс Лист'
        verbose_name_plural = u'Прайс Листы'
        ordering = ['id']

    def __unicode__(self):
        return self.name


class Price(models.Model):

    price_list = models.ForeignKey(PriceList, verbose_name=u'Прайс Лист')
    name = models.CharField(max_length=255, verbose_name=u'Название Услуги')
    price = models.CharField(max_length=255, verbose_name=u'Цена')

    class Meta:
        verbose_name = u'Цена'
        verbose_name_plural = u'Цены'
        ordering = ['price_list', 'name', 'price']


class Document(models.Model):

    name = models.CharField(max_length=255, verbose_name=u'Название')
    order = models.IntegerField(verbose_name=u'Место в списке')

    class Meta:
        verbose_name = u'Документ'
        verbose_name_plural = u'Документы'
        ordering = ['order']

    def __unicode__(self):
        return self.name


class DocumentImage(models.Model):

    document = models.ForeignKey(Document, verbose_name=u'Документ')
    image = models.ImageField(verbose_name=u'Изображение', upload_to='')

    class Meta:
        verbose_name = u'Изображение документа'
        verbose_name_plural = u'Изображения документа'

    def __unicode__(self):
        return u'{} {}'.format(self.document.name, self.image.name)


class Photo(models.Model):

    photo = models.ImageField(verbose_name=u'Фотография', upload_to='')

    class Meta:
        verbose_name = u'Фотография'
        verbose_name_plural = u'Фотографии'

    def __unicode__(self):
        return self.photo.url


class Contact(models.Model):

    address = models.CharField(max_length=255, verbose_name=u'Адрес')
    map = models.CharField(max_length=255, verbose_name=u'Адрес для карты')
    schedule = models.CharField(max_length=255, verbose_name=u'Расписание')
    city_number = models.CharField(max_length=255, verbose_name=u'Городской телефон')
    mobile_phone = models.CharField(max_length=255, verbose_name=u'Мобильный телефон')
    email = models.CharField(max_length=255, verbose_name=u'Почта')
    ceo = models.CharField(max_length=255, verbose_name=u'Директор')

    class Meta:
        verbose_name = u'Контакт'
        verbose_name_plural = u'Контакты'
