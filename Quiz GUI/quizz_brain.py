import html


class Brains:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_bank = q_list
        self.q_text = None
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        self.current_question = self.question_bank[self.question_number]
        self.question_number += 1
        self.q_text = html.unescape(self.current_question.text)
        return self.q_text

    def check_answer(self, user_answer: str):
        if self.current_question.ans == user_answer:
            self.score += 1
            return True
        else:
            return False

