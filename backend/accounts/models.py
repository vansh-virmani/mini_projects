from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile( models.Model):
     
     

     LANGUAGE_CHOICES = [
        ("python", "Python"),
        ("c", "C"),
        ("cpp", "C++"),
    ]
     EXPERIENCE_CHOICES = [
        ('beginner',     'Less than 6 months'),
        ('intermediate', '6 months to 2 years')
        # ('advanced',     'More than 2 years'),
    ]
     
     user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
     language=models.CharField( max_length=50, choices= LANGUAGE_CHOICES,default='python')
     experience  = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='beginner')
     streak      = models.IntegerField(default=0)
     last_active = models.DateField(null=True, blank=True)
     created_at  = models.DateTimeField(auto_now_add=True)



    

   

     def __str__(self):
        return f"{self.user.username}'s profile"
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:                              # only on NEW user, not on update
        UserProfile.objects.create(user=instance)




#signal must be registered an apps.py and settings.py