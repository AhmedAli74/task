from django.db import models
from django.urls import reverse
from exams.models import Category
from django.utils.text import slugify
# Create your models here.
class Subject(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subject_name=models.CharField(max_length=200)
    slugy=models.SlugField(unique=True,blank=True,null=True)
    hours=models.IntegerField(default=0)
    time=models.DateTimeField(auto_now=True)
    is_available=models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        self.slugy=slugify(self.subject_name)
        super(Subject,self).save(*args,**kwargs)

    def get_url(self):
        return reverse('Exams:subjects_slug',args=[self.category.slug,self.slugy])

    class Meta:
        verbose_name=("Subject")
        verbose_name_plural=("Subjects")
    
    def __str__(self):
        return self.subject_name
