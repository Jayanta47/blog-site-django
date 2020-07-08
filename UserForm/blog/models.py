from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_site:post-detail', kwargs={'pk': self.pk})

# difference between redirect and reverse
# redirect itself makes a request on the views
# and takes to that page/ redirect to a specific route
# but reverse will simply return the full url
# to which the page will go and views will eventually
# manage it.
