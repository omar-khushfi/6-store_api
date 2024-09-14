from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    reset_password_token=models.CharField(max_length=50,blank=True,default="")
    reset_password_exprire=models.DateTimeField(null=True,blank=True)
    
    
@receiver(post_save, sender=User)
def save_profile(sender,instance,created, **kwargs):
    user=instance
    if created:
        profile=Profile(user=user)
        profile.save()