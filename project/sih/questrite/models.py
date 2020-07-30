from django.db import models

# Create your models here.

class QuestionsP(models.Model):
    questions =  models.TextField()
    answers = models.CharField(max_length = 100, blank = True, null = True)    

class QuestionsSchool(models.Model):
    questions_s = models.TextField()
    answers_s = models.CharField(max_length = 100, blank = True, null = True)

class QuestionsGraduates(models.Model):
    questions_g = models.TextField()
    answers_g = models.CharField(max_length = 100, blank = True, null = True)

class QuestionsDropouts(models.Model):
    questions_d = models.TextField()
    answers_d = models.CharField(max_length = 100, blank = True, null = True)

