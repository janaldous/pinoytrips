from django.db import models


class Destination(models.Model):
	name = models.CharField(max_length=200)
	region = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Terminal(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	region = models.CharField(max_length=200)
	
	def __str__ (self):
		return self.name
	
class Operator(models.Model):
	RATING_CHOICES = (
		('non-ac', 'Non-airconditioned'),
		('ac', 'Airconditioned'),
		('business', 'Business'),
	)
	
	name = models.CharField(max_length=200)
	rating = models.CharField(max_length=10, default='Non-ac', choices=RATING_CHOICES)
	features = models.CharField(max_length=200, blank=True)
	address = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	website = models.URLField(max_length=200, blank=True)
	terminal = models.ForeignKey(Terminal)
	destination = models.ForeignKey(Destination)
	
	def __str__(self):
		return self.name
	
# Create your models here.
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
	
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''