from django.db import models


class Journalist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Article (models.Model):
    author = models.ForeignKey(Journalist,
                               on_delete=models.CASCADE,
                               related_name='articles')
    # author = models.CharField(max_length=50)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # difference between auto_now_add and auto_now is that auto_now_add is
    # invoked only when the creation of a new instance occurs.

    def __str__(self):
        return f'{self.author} {self.title}'
