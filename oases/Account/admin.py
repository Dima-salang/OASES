# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Student, Teacher, Section

# Define an inline admin descriptor for Student model which acts a bit like a singleton
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'
    fk_name = 'user'

# Define an inline admin descriptor for Teacher model which acts a bit like a singleton
class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = 'teacher'
    fk_name = 'user'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline, TeacherInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Section)