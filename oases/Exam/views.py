from django.shortcuts import render, redirect
from .forms import ExamPDFForm
from .utils import parse_pdf
from .models import Exam, Question, Choice, AnswerExam
from .forms import ExamPDFForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

# Create your views here.
def upload_exam(request):
    if request.method == 'POST':
        form = ExamPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['exam_pdf']
            fs = FileSystemStorage()
            filename = fs.save(pdf_file.name, pdf_file)
            file_path = fs.path(filename)

            questions_data = parse_pdf(file_path)

            exam = form.save(commit=False)
            exam.teacher = request.user.teacher
            exam.save()

            for question_data in questions_data:
                question = Question.objects.create(exam=exam, question_text=question_data['question_text'])
                for label, choice_text in question_data['choices'].items():
                    Choice.objects.create(question=question, choice_text=choice_text)
                for answer in question_data['correct_answer']:
                    AnswerExam.objects.create(question=question, answer=answer)
            return redirect("home")
    else:
        form = ExamPDFForm()
    return render(request, 'upload_exam.html', {'form': form})