from django.db import models

from django.urls import reverse


# Create your models here.


class Blog(models.Model):

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_absolute_url(self):
        """
        Return the absolute URL for the blog API detail with the given primary key.
        """

        return reverse("blog_api_retrieve", kwargs={"pk": self.pk})
