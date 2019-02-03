from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import JSONField
import hashlib
from colorful.fields import RGBColorField
from django.template.defaultfilters import slugify


# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200)
    image_category = models.ImageField(null = True, blank = True, upload_to = 'Category_images')
    color = RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF', '#17a589'])




    def __str__(self):
        return self.name









class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank = True, upload_to = 'Avatar', default= 'Avatar/deafult-profile-image.png')
    firstname = models.CharField(max_length = 500, blank = True, null = False)
    email = models.EmailField(max_length=254, blank = True, null = False)
    relation = models.CharField(max_length = 500, blank = True, null = True)
    pays = models.CharField(max_length = 500, blank = True, null = True)

    def __str__(self):
        return self.name.username


class articles(models.Model):
    article_author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, max_length=200, on_delete=models.CASCADE)
    avatar = models.ForeignKey(author, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)


    title = models.CharField('العنوان', max_length=200)
    image = models.ImageField('صورة مناسبة', upload_to = 'Images')
    prix = models.IntegerField('سعر الكلوغرام الواحد بالتجزئة / الدينار')
    prix_colobal = models.IntegerField('سعر الكلوغرام الواحد بالجملة /الدينار' )
    body = models.TextField('وصف المنتج', max_length = 500)
    number = models.IntegerField('رقم الهاتف')
    wilaya = models.CharField('الولاية', max_length=200)
    baladiya = models.CharField('البلدية', max_length=200)

    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)





    def __str__(self):
        return '%s %s %s' % (self.title, '/', self.category)




    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blogArabic:show_article', args =[str(self.id)])

def get_image_filename(instance, filename):

        title = instance.post.title
        slug = slugify(title)
        return "post_images/%s-%s" % (slug, filename)





class MyltiImage(models.Model):
      post = models.ForeignKey(articles, on_delete=models.CASCADE)
      image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')






class contactModel(models.Model):


    username1 = models.CharField(max_length = 500, blank = True, null = True)
    email = models.CharField(max_length = 500, blank = True, null = True)
    text_body = models.TextField(max_length = 500, blank = True, null = True)

    def __str__(self):
        return self.username1




class comment_put(models.Model):

    user_comment = models.ForeignKey(User, default = None, on_delete = models.CASCADE)
    user_put = models.ForeignKey(articles, on_delete = models.CASCADE)
    avatar_commenter = models.ForeignKey(author, on_delete = models.CASCADE)
    comment = models.TextField(max_length = 500)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.comment
