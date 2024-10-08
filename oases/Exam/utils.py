# exams/utils.py
import pdfplumber
import re

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
