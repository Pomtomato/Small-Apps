from tkinter import *
from quizz_brain import Brains

THEME_COLOR = "#B1DDC6"


class QuizzInterface:
    # self.score = points
    # self.question = questions
    def __init__(self, quiz_brain: Brains):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        bg_img = PhotoImage(file="./Small-Apps/Quiz GUI/images/card_front.png")
        self.canvas = Canvas(width=800, height=526)
        self.canvas.config(highlightthickness=0, bg=THEME_COLOR)
        self.canvas.create_image(400, 263, image=bg_img)

        self.score_text = self.canvas.create_text(700, 30, text=f"Score: 0",
                                                  font=("Ariel", 20, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2, pady=50)
#------------------------
        self.prompt_canvas = Canvas(width=600, height=300)
        self.prompt_canvas.config(highlightthickness=0, bg="white")
        self.question_text = self.prompt_canvas.create_text(300, 150, text="",
                                                            width=500, font=("Ariel", 20, "bold"))
        self.prompt_canvas.grid(row=0, column=0, columnspan=2)
#----------------------------
        right_img = PhotoImage(file="./Small-Apps/Quiz GUI/images/true.png")
        self.right_button = Button(image=right_img)
        self.right_button.config(bg=THEME_COLOR, highlightthickness=0, command=self.green_button)
        self.right_button.grid(row=1, column=0)

        wrong_img = PhotoImage(file="./Small-Apps/Quiz GUI/images/false.png")
        self.wrong_button = Button(image=wrong_img)
        self.wrong_button.config(bg=THEME_COLOR, highlightthickness=0, command=self.red_button)
        self.wrong_button.grid(row=1, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.prompt_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.quiz.score}")
            self.prompt_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.prompt_canvas.itemconfig(self.question_text, text="Thank you for playing")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def green_button(self):
        prompt = self.quiz.check_answer("True")
        self.give_feedback(prompt)

    # does the same thing 2 line vs 1 line
    def red_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, prompt):
        if prompt:
            self.prompt_canvas.config(bg='green')
            self.window.after(1000, self.get_next_question)

        else:
            self.prompt_canvas.config(bg='red')
            self.window.after(1000, self.get_next_question)



