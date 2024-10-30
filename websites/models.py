from django.db import models
from django.contrib.auth.models import User

class Website(models.Model):
    name = models.CharField('网站名称', max_length=200)
    url = models.URLField('网站地址')
    description = models.TextField('网站描述')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '网站'
        verbose_name_plural = '网站'

    def __str__(self):
        return self.name