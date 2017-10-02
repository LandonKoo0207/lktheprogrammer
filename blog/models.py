from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from datetime import datetime
from tinymce import HTMLField

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    contents = HTMLField()
    category = models.ForeignKey(Category)
    time_updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    # Update the time updated when saved
    def save(self, *args, **kwargs):
        self.time_updated = datetime.now()
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_summary(self):
        return self.contents[:550]

    def get_absolute_url(self):
        return reverse('post_update', kwargs={'pk': self.pk})
