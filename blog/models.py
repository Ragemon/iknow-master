from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from tinymce.models import HTMLField






# Create your models here.
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
        ('sketch', 'Sketch'),
    )
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(default='Courage', max_length=150)
    created = models.DateTimeField(auto_now=False,
                                     auto_now_add=True,
                                   null=True)

    update = models.DateTimeField(auto_now=True,
                                  auto_now_add=False)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    slug = models.SlugField(max_length=1100, unique_for_date='created')

    comments = models.BooleanField(default=True)
##install Pillow from pip install Pillow to use image
    post_image = models.ImageField(upload_to='blog-image',blank=True)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         'blog:article-list',
    #
    #     )






