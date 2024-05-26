from django.db import models
from django.urls import reverse
from subjects.models import Subject
# Create your models here.

class QuestionMCQ(models.Model):
    subjects=models.ForeignKey(Subject,on_delete=models.CASCADE)
    questions=models.TextField(max_length=700)
    answer1=models.TextField(max_length=200)
    answer2=models.TextField(max_length=200)
    answer3=models.TextField(max_length=200)
    answer4=models.TextField(max_length=200)
    is_active=models.BooleanField(default=True)

    class Meta:
        verbose_name=("QuestionMCQ")
        verbose_name_plural=("QuestionMCQ's")
    
    def __str__(self):
        return str(self.subjects)
    
class Question(models.Model):
    question_id = models.IntegerField(default=0)
    subjects=models.ForeignKey(Subject,on_delete=models.CASCADE)
    questions=models.TextField(max_length=700)
    is_active=models.BooleanField(default=True)
    class Meta:
        verbose_name=("Question")
        verbose_name_plural=("Questions")
    
    def __str__(self):
        return str(self.subjects)
    
    def get_urll(self):
        return reverse('Exams:score_id',args=[self.subjects.slugy,self.question_id])

class Answrer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answers=models.TextField(max_length=700)
    is_active=models.BooleanField(default=True)

    class Meta:
        verbose_name=("Answrer")
        verbose_name_plural=("Answrers")
    
    def __str__(self):
        return str(self.subjects)
