from django.db import models
from Account import models as Account
# Create your models here.

class Exam(models.Model):
    teacher = models.ForeignKey(Account.Teacher, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=100)
    exam_subject = models.CharField(max_length=100)
    exam_date = models.DateField()

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField()


class AnswerChoice(models.Model):
    student = models.ForeignKey(Account.Student, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    answer = models.SmallIntegerField()

class AnswerExam(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.SmallIntegerField()
