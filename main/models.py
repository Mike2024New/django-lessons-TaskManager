from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('название',max_length=100)
    task = models.TextField('описание')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"