from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):

    class Meta:
        db_table = 'student'

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_id = models.CharField(max_length=100, primary_key=True)
    student_section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.student_id


class Teacher(models.Model):

    class Meta:
        db_table = 'teacher'

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    teacher_id = models.CharField(max_length=100, primary_key=True)
    teacher_name = models.CharField(max_length=100)


    def __str__(self):
        return self.teacher_name


class Section(models.Model):

    class Meta:
        db_table = 'section'

    section_id = models.CharField(max_length=100, primary_key=True)
    section_name = models.CharField(max_length=100)
    teacher_handle = models.ForeignKey(Teacher, on_delete=models.CASCADE)


    def __str__(self):
        return self.section_name
