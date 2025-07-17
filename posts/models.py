from django.db import models

"SELECT * FROM posts; --> Post.object.all()"
"SELECT * FROM posts WHERE title ILIKE('%post%');--> Post.object.filter(title__icontains='post')"
"SELECT 1 FROM posts WHERE id=1;--> Post.object.get(id=1)"

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=456)
    rate = models.IntegerField(default=0,null=True)


    def __str__(self):
        return f"{self.title}-{self.content}"