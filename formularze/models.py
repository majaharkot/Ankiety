from django.db import models

class Pytanie(models.Model):
    pytanie = models.CharField(verbose_name='pytanie', max_length=100)

    def __str__(self):
        return self.pytanie

    class Meta:
        verbose_name_plural = 'pytania'
