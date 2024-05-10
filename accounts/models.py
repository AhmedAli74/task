from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

def Upload_profile(instance,file_name):
    extention=file_name.split('.')[1]
    return f'prof/{instance.user}.{extention}'

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=Upload_profile,width_field=None,height_field=None)
    email=models.EmailField(max_length=200)
    phone=models.IntegerField(default=0)

    class Meta:
        verbose_name=("Profile")
        verbose_name_plural=("Profiles")

    def __str__(self):
        return str(self.user)

    @receiver(post_save,sender=User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

