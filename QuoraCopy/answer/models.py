from django.db import models
from account.models import QuoraUser
from question.models import Question
# Create your models here.

class Answer(models.Model):
	rich_text = models.TextField(max_length = 8192,blank=False,null=False)
	by = models.ForeignKey(QuoraUser,related_name="user_answers")
	pub_time = models.DateTimeField(auto_now_add = True)
	on = models.ForeignKey(Question,related_name="question_answers")
	views_count = models.IntegerField(default = 0)
	upvotes = models.ManyToManyField(QuoraUser,related_name="answer_upvotes")
	downvotes = models.ManyToManyField(QuoraUser,related_name="answer_downvotes")

