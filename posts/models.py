from django.db import models

"SELECT * FROM posts; --> Post.object.all()"
"SELECT * FROM posts WHERE title ILIKE('%post%');--> Post.object.filter(title__icontains='post')"
"SELECT 1 FROM posts WHERE id=1;--> Post.object.get(id=1)"

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=456)
    rate = models.IntegerField(default=0,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.title}-{self.content}"