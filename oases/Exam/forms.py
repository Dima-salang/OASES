from django import forms
from .models import Exam
class ExamPDFForm(forms.ModelForm):
    exam_pdf = forms.FileField(label='Upload Exam PDF')

    class Meta:
        model = Exam
        fields = ['exam_name', 'exam_subject', 'exam_date']

        widgets = {
            'exam_date': forms.DateInput(attrs={'type': 'date'}),
        }

