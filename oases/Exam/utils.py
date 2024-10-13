# exams/utils.py
import pdfplumber
import re
from .models import AnswerChoice

def parse_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

        # Extract questions, choices, and answers using regular expressions
        question_pattern = re.compile(r'(\d+)\.\s(.+?)(?=\n[A-D]\))', re.DOTALL)
        choices_pattern = re.compile(r'([A-D])\)\s(.+?)(?=\n[A-D]\)|Answer:)', re.DOTALL)
        answer_pattern = re.compile(r'Answer:\s([A-D])')

        # Split the text into sections for each question
        questions_data = []
        questions_matches = question_pattern.findall(text)
        for question_match in questions_matches:
            question_number, question_text = question_match

            # Find the choices for the current question
            choices_matches = choices_pattern.findall(text)

            choices = {}
            for choice_match in choices_matches:
                choice_label, choice_text = choice_match
                choices[choice_label] = choice_text.strip()

            # Find the correct answer
            answer_match = answer_pattern.search(text)
            correct_answer = answer_match.group(1) if answer_match else None

            questions_data.append({
                'question_text': question_text.strip(),
                'choices': choices,
                'correct_answer': correct_answer
            })

        return questions_data


def check_answers(student_answers, correct_answers):
    print("Checking answers...")

    # load everything into memory
    correct_answers_dict = {answer.question.pk: answer.answer for answer in correct_answers}
    print(correct_answers_dict)

    # create a list to track the answers to update
    answer_choices_to_update = []

    for student_answer in student_answers:
        # check if the answer is correct
        student_answer.is_correct = student_answer.choice.question.pk in correct_answers_dict and student_answer.answer == correct_answers_dict[student_answer.choice.question.pk]

        if student_answer.is_correct:
            answer_choices_to_update.append(student_answer)

        print(f"Student: {student_answer.student.student_id}, Choice = {student_answer.choice.choice_text}, Answer Label: {student_answer.answer}, Correct = {student_answer.is_correct}")
    print(answer_choices_to_update)

    # bulk update to prevent individual db queries
    AnswerChoice.objects.bulk_update(answer_choices_to_update, ['is_correct'])



def calculate_stats(exam):
    print("Calculating stats...")
    print("stats")