from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.template.defaultfilters import slugify

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=5000)
    head0 = models.CharField(max_length=50)
    chead0 = models.CharField(max_length=5000,default="")
    head1 = models.CharField(max_length=50)
    chead1 = models.CharField(max_length=5000,default="")
    head2 = models.CharField(max_length=50)
    chead2 = models.CharField(max_length=5000,null=True,blank=True)
    pub_date = models.DateTimeField(auto_now_add=credits)
    thumbnail = models.ImageField(upload_to='blog/images', default="")
    slug = models.SlugField()
    likes = models.ManyToManyField(User,related_name='likes')

    @property
    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
       self.slug = slugify(self.user.username)
       super(Blogpost,self).save(*args,**kwargs)


class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
   # parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment + " by " + self.user.username