from django.contrib import admin

from .models import Answer
# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
	fields = ['rich_text','by','on']

admin.site.register(Answer,AnswerAdmin)
