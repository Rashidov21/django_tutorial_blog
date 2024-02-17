from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Category name",max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    
    def __str__(self):
        return str(self.name)
    
    
class Tag(models.Model):
    name = models.CharField(verbose_name="Tag name",max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    
    def __str__(self):
        return str(self.name)


class Post(models.Model):
    title = models.CharField(verbose_name="Post title",max_length=550)
    body = models.TextField(verbose_name="Post body")
    author = models.CharField(verbose_name="Post author",default="Admin",max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,related_name='posts')
    tag = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(verbose_name="Published time",auto_now_add=True)
    published = models.BooleanField(default=True)
    on_top = models.BooleanField(default=False)
    
    
    def get_avg_rating(self):
        # print([int(i.value) for i in self.ratings.all()])
        sum_ratings = sum([int(i.value) for i in self.ratings.all()])
        try:
            return round(sum_ratings / self.ratings.all().count(),2)
        except Exception as e:
            return 0     
    
    def __str__(self):
        return str(self.title)
    

class Comment(models.Model):
    author = models.CharField(verbose_name="Comment author",max_length=100,blank=False)
    comment = models.TextField(verbose_name="Comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    
    def __str__(self):
        return str(self.author)
    
    
class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveSmallIntegerField(verbose_name="Post rating",default=0)
    
    def __str__(self):
        return str(self.value)