from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)

class Article(models.Model):
	image = models.ImageField(upload_to=upload_to, blank=True, null=True)
	style = models.ImageField(upload_to=upload_to, blank=True, null=True)


	def __str__(self):
		return self.title