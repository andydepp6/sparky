from django.db import models

# Create your models here.

class Register(models.Model):

	name = models.CharField(max_length=300,null=False,blank=False)
	email = models.CharField(max_length=200,null=False,blank=False)

	def __unicode__(self):
		return self.name
