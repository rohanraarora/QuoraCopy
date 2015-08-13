from django.contrib import admin
from .models import *
# Register your models here.
class TopicAdmin(admin.ModelAdmin):
	fields = [ 'name','desc','pic','related_topics']


admin.site.register(Topic,TopicAdmin)
