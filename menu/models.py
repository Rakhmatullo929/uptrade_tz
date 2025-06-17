from django.db import models
from django.urls import reverse, NoReverseMatch
from django.db.models import CASCADE

class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название меню")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, CASCADE, related_name="items", verbose_name="Меню")
    title = models.CharField(max_length=200, verbose_name="Название пункта")
    url = models.CharField(max_length=200, blank=True, verbose_name="URL")
    named_url = models.CharField(max_length=100, blank=True, verbose_name="Named URL")
    parent = models.ForeignKey('self', CASCADE, blank=True, null=True, 
                              related_name="children", verbose_name="Родительский пункт")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")
    
    def __str__(self):
        return self.title
    
    def get_url(self):
        """Возвращает URL пункта меню"""
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return "#"
        return self.url if self.url else "#"
    
    def get_absolute_url(self):
        """Получает абсолютный URL для пункта меню"""
        return self.get_url()
    
    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ['order', 'title']
