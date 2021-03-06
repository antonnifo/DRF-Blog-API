from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class BaseContent(models.Model):
  
    publish  = models.DateTimeField(default=timezone.now)            
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    
    class Meta:
        abstract = True

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
        self).get_queryset().filter(status='published')


class Category(BaseContent):
        name = models.CharField(max_length=200)
        slug = models.SlugField(max_length=200,
                    unique=True)

        def save(self, *args, **kwargs):
            '''overrides save action'''
            
            if not self.slug and self.name:
                self.slug = slugify(self.name)

            super(Category, self).save(*args, **kwargs)                     
        class Meta:
            ordering = ('updated',)
            verbose_name = 'category'
            verbose_name_plural = 'categories'

        def __str__(self):
            return self.name


class Post(BaseContent):
    
    published = PublishedManager() # custom manager.
    
    
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250, unique_for_date='publish',)
    author  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body    = models.TextField()
    category       = models.ForeignKey(Category,
                        related_name='posts',
                                on_delete=models.CASCADE) 
    status   = models.CharField(max_length=10, choices =STATUS_CHOICES, default='draft')
    
    def save(self, *args, **kwargs):
        '''overrides save action'''
        
        if not self.slug and self.title:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)       
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
