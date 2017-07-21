from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)
