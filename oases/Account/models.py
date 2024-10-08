from django.db import models

# Create your models here.
class Student(models.Model):

    class Meta:
        db_table = 'student'

    student_id = models.CharField(max_length=100, primary_key=True)
    student_name = models.CharField(max_length=100)
    student_username = models.CharField(max_length=100)
    student_password = models.CharField(max_length=100)
    student_section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)


class Teacher(models.Model):

    class Meta:
        db_table = 'teacher'

    teacher_id = models.CharField(max_length=100, primary_key=True)
    teacher_name = models.CharField(max_length=100)
    teacher_username = models.CharField(max_length=100)
    teacher_password = models.CharField(max_length=100)


class Section(models.Model):

    class Meta:
        db_table = 'section'

    section_id = models.CharField(max_length=100, primary_key=True)
    section_name = models.CharField(max_length=100)
    teacher_handle = models.ForeignKey(Teacher, on_delete=models.CASCADE)
