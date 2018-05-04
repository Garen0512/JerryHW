from django.db import models

# Create your models here.
class Mother(models.Model):
	content = models.CharField(max_length=1000)

	def __str__(self):
		return self.comment