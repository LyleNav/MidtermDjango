from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField("Date Created", auto_now_add=True)
    date_updated = models.DateTimeField("Date Updated", null=True, blank=True, auto_now=True)
    content = models.TextField(max_length=100)
    is_active = True

    def __str__(self):
        return 'Post: {}'.format(self.content)

class Comment(models.Model):
    date_created = models.DateTimeField("Date Created")
    content = models.TextField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "comments", null=True, blank=True)

    def __str__(self):
        return 'Comment: {}'.format(self.content)