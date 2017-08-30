from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import now
from datetime import datetime
#from ckeditor import fields
from froala_editor import fields
from bs4 import BeautifulSoup

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    contents = fields.FroalaField()
    category = models.ForeignKey(Category)
    time_updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    # Update the time updated when saved
    def save(self, *args, **kwargs):
        self.time_updated = datetime.now()
        super(Post, self).save(*args, **kwargs)

    def content_str(self):
        soup = BeautifulSoup(self.contents, "html.parser")
        return soup.get_text()

    def get_absolute_url(self):
        return reverse('post_update', kwargs={'pk': self.pk})
