from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce import HTMLField
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField('Post Content')
    published = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})