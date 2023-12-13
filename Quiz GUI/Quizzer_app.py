from data import question_data
from question_model import Question_object
from quizz_brain import Brains
from ui import QuizzInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_category = question["category"]
    new_question = Question_object(question_text, question_answer, question_category)
    question_bank.append(new_question)

quiz = Brains(question_bank)
try:
    quiz_interface = QuizzInterface(quiz)
except IndexError:
    quiz_interface.end_messege()
