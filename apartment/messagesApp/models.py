from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
	message_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	sent_by = models.CharField(max_length=100)
	sent_to = models.CharField(max_length=100)
	urgency = models.IntegerField()

	def __str__(self):
		return self.message_text
