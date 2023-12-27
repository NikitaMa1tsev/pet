from django.db import models

# Create your models here.


class DataTest(models.Model):
	name = models.CharField(max_length=255)

	# class Meta:
	# 	verbose_name = _("")
	# 	verbose_name_plural = _("s")

	def __str__(self):
			return self.name
