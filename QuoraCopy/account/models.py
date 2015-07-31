from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class QuoraUser(AbstractUser):
	bio = models.CharField(max_length = 128,blank = True,null = True)
	desc = models.TextField(max_length = 8192,blank = True,null=True)
	profile_pic = models.ImageField(upload_to = "/profile_pics",blank = True)
	following = models.ManyToManyField("self", symmetrical = False, related_name = "followers")
