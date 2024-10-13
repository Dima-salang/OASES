from typing import Any
from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Exam.models import Exam, Question, Choice, AnswerExam, AnswerChoice
from Exam.utils import check_answers
# Create your views here.

class HomeView(ListView):
    template_name = "home.html"
    context_object_name = "exams"

    def get_queryset(self) -> QuerySet[Any]:
        context = Exam.objects.all()
        return context
    

class ExamView(DetailView):
    template_name = "exams/exam_details.html"
    model = Exam

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["questions"] = Question.objects.filter(exam=self.object)
        return context
    

def start_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    questions = Question.objects.filter(exam=exam)

    print(f"Exam: {exam.__str__()} Questions: {questions}")

    if request.method == 'POST':
        # Process the form data
        student = request.user.student

        for question in questions:
            # get the user's answer
            answer = request.POST.get(f'question_{question.pk}')
            if answer:
                # unpack the pk of the choice and the actual label
                choice_pk, ans_label = answer.split("-")

                print(f"Answer label: {ans_label}")

                # transform the ans_label to the corresponding choice character
                ans_label = chr(int(ans_label)+64)

                # get the choice object from the pk
                choice = Choice.objects.get(pk=choice_pk)
                print(f"Choice PK: {choice_pk} Choice Label: {ans_label}")

                # create the user choice object
                AnswerChoice.objects.create(student=student, choice=choice, answer=ans_label, is_correct=False)
        student_answers = AnswerChoice.objects.filter(student=student, choice__question__exam=exam)
        correct_answers = AnswerExam.objects.filter(question__exam=exam)
        print(correct_answers)
        check_answers(student_answers, correct_answers)




    return render(request, 'exams/exam_start.html', {'exam': exam, 'questions': questions})



class TeacherExamDashboard(ListView):
    template_name = "teachers/teacher_dashboard.html"
    context_object_name = "exams"

    def get_queryset(self) -> QuerySet[Any]:
        context = Exam.objects.filter(teacher=self.request.user.teacher)
        return context
    

class TeacherExamView(DetailView):
    template_name = "teachers/exam_stats.html"
    model = Exam

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["questions"] = Question.objects.filter(exam=self.object)
        return context
    
    