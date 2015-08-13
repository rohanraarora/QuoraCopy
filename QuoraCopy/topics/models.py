from django.db import models
# Create your models here.

class Topic(models.Model):
	name = models.CharField(max_length = 128,blank = False,null = False)
	desc = models.TextField(max_length = 8192,blank = True,null = True)
	pic = models.ImageField(upload_to = "/topics/pics")
	followers_count = models.IntegerField(default = 0)
	related_topics = models.ManyToManyField("self",related_name = "related_topics")

	def __str__(self):
		return self.name

