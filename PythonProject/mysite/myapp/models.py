

from django.db import models
from django.urls import reverse

# Create your models here

class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.emoji

class ShavarmaStore(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    rating = models.IntegerField()
    network = models.BooleanField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shavarma_store_detail', kwargs={'pk': self.pk})

    def stars_display(self):
        return '★' * self.rating + '☆' * (5 - self.rating)


class Food(models.Model):
    name = models.CharField(max_length=100)
    shavarma_store = models.ForeignKey(ShavarmaStore, on_delete=models.CASCADE)
    spicy = models.BooleanField()
    rating = models.IntegerField()
    price = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    ingredients = models.ManyToManyField(Ingredients, blank=True, related_name='food')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food_detail', kwargs={'pk': self.pk})

    def stars_display(self):
        return '★' * self.rating + '☆' * (5 - self.rating)


