from django.db import models
from django.urls import reverse, NoReverseMatch

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID", help_text="Уникальный идентификатор пункта меню")
    title = models.CharField(max_length=200, verbose_name="Название пункта меню")
    menu_name = models.CharField(max_length=100, verbose_name="Название меню")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, verbose_name="Родительский пункт")
    url = models.CharField(max_length=200, blank=True, verbose_name="URL (явный)")
    named_url = models.CharField(max_length=100, blank=True, verbose_name="Named URL")
    order = models.IntegerField(default=0, verbose_name="Порядок")

    def get_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'  # Или другой обработчик ошибки
        return '#'  # Или другой обработчик ошибки

    def __str__(self):
        return f"{self.title} ({self.menu_name})"

    class Meta:
        ordering = ['order']
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"