from django.db import models
from django.urls import reverse
# Create your models here.


class Author(models.Model):
    name = models.CharField(null=False, max_length=250, blank=False)

    def get_absolute_url(self):
        return reverse('books:author_detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(null=False, max_length=250, blank=False)
    author = models.ForeignKey(
        Author, null=False, blank=False, on_delete=models.CASCADE, related_name='book_author')
