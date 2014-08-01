from django.db import models
from django import forms
from django.forms.widgets import RadioSelect

class Student(models.Model):
	userid = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	gtid = models.CharField(max_length=12)
	lastname = models.CharField(max_length=50)
	firstname = models.CharField(max_length=50)

	def __unicode__(self):
		return self.userid

class Question(models.Model):
	text = models.CharField(max_length=500)

	def __unicode__(self):
		return self.text

class Answer(models.Model):
	question_id = models.IntegerField()
	student_id = models.IntegerField()
	answer = models.CharField(max_length=500)
	answer_tf = models.CharField(max_length=20)
	score = models.FloatField(default=0.0)

	def __unicode__(self):
		return str(self.student_id) + "'s answer to q" + str(self.question_id)

class TFLog(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	student_id = forms.IntegerField()
	question_id = forms.IntegerField()

class MCLog(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	student_id = forms.IntegerField()
	answer1_id = forms.IntegerField()
	answer2_id = forms.IntegerField()

class TFForm(forms.Form):
	answer_tf = forms.ChoiceField(
			widget=RadioSelect(),
			choices=[['1','True'],['0','False']])
	answer = forms.CharField(required=True)
	fields = ('answer', 'explanation')

class MCForm(forms.Form):
	choice = forms.ChoiceField(
			widget=RadioSelect(),
			choices=[['1','First is True'],
					['2','Second is True'],
					['3', 'Both are True'],
					['4', 'Both are False']])


class Score(models.Model):
	answer_id = models.IntegerField()
	scorer_id = models.IntegerField()
	score = models.IntegerField()

	def __unicode__(self):
		return str(self.scorer_id) + "'s score for a" + str(self.answer_id)
