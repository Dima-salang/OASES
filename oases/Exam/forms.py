from django import forms

class ExamPDFForm(forms.Form):
    exam_pdf = forms.FileField(label='Upload Exam PDF')
    