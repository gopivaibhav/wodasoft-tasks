from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.JSONField('Article title', default=dict)
    default = models.CharField(max_length=5, default='en')
    def __str__(self):
        return self.title['en']
    class Meta:
        verbose_name_plural = "Articles!!"