from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
def Upload(instance,file_name):
    extention=file_name.split('.')[1]
    return f'grade/{instance.name_category}.{extention}'


class Category(models.Model):
    name_category=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,blank=True,null=True)
    image=models.ImageField(upload_to=Upload,width_field=None,height_field=None)
    faculaty=models.CharField(max_length=200)
    count_of_subjects=models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name_category)
        super(Category,self).save(*args,**kwargs)

    def get_url(self):
        return reverse('Exams:category_slug',args=[self.slug])


    class Meta:
        verbose_name=("Category")
        verbose_name_plural=("Categories")
    
    def __str__(self):
        return self.name_category