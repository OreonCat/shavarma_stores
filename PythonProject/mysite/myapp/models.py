from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

class RatingField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
        kwargs['default'] = kwargs.get('default', 0)
        super().__init__(*args, **kwargs)

class Ingredients(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    emoji = models.CharField(max_length=100, verbose_name="Эмодзи")

    def __str__(self):
        return self.name + " " + self.emoji

    class Meta:
        verbose_name_plural = "Ингредиенты"
        verbose_name = "Ингредиенты"

class ShavarmaStore(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    logo = models.ImageField(upload_to='logo', null=True, blank=True, default=None, verbose_name="Логотип")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    rating = RatingField(verbose_name="Рейтинг")
    network = models.BooleanField(verbose_name="Сетевая")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Шаурмечные"
        verbose_name = "Шаурмечная"

    def get_absolute_url(self):
        return reverse('shavarma_store_detail', kwargs={'pk': self.pk})

    def stars_display(self):
        return '★' * self.rating + '☆' * (5 - self.rating)



class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    shavarma_store = models.ForeignKey(ShavarmaStore, on_delete=models.CASCADE, verbose_name="Шаурмечная", related_name="food")
    spicy = models.BooleanField(verbose_name="Острый")
    rating = RatingField(verbose_name="Рейтинг")
    price = models.IntegerField(verbose_name="Цена")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    ingredients = models.ManyToManyField(Ingredients, blank=True, related_name='food')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Блюда"
        verbose_name = "Блюдо"

    def get_absolute_url(self):
        return reverse('food_detail', kwargs={'pk': self.pk})

    def stars_display(self):
        return '★' * self.rating + '☆' * (5 - self.rating)


