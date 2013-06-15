from django.db import models

class Person(models):
	name = models.CharField(max_length = 100)
	age = models.CharField(max_length = 100)