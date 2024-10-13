
from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('exam/<int:pk>/', ExamView.as_view(), name='exam_detail'),
    path('exam//start/<int:pk>/', start_exam, name='start_exam'),
    path('teacher_dashboard/exams/', TeacherExamDashboard.as_view(), name='teacher_dashboard'),

]