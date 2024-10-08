from django.shortcuts import render, redirect
from .forms import ExamPDFForm
from .utils import parse_pdf
from .models import Exam, Question, Choice
from django.http import HttpResponse

# Create your views here.
