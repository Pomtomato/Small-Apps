import pandas
from tkinter import *
from tkinter import messagebox
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)

#
# # ------------NEXT FLASHCARD----------#
# def next_card():
#     global current_card
#     current_card = random.choice(to_learn)
#     french_word = current_card['French']
#     french_front(french_word)
#     window.after(3000, flip_card)
#
#
# #-------------FLIP FLASHCARD----------#
# def flip_card():
#     global current_card
#     english_word = current_card['English']
#     english_back(english_word)
#
#
# #------------UI DESIGN---------------#
# window = Tk()
# window.title("Frenchly")
# window.config(bg=BACKGROUND_COLOR, padx=80, pady=50)
#
# bg_front_png = PhotoImage(file="images/card_front.png")
#
#
# def french_front(word):
#     bg_front = Canvas(width=800, height=526)
#     bg_front.create_image(400, 263, image=bg_front_png)
#     bg_front.config(bg=BACKGROUND_COLOR, highlightthickness=0)
#     card_title = bg_front.create_text(400, 150, fill="black", text="French", font=(FONT_NAME, 20, "italic"))
#     card_word = bg_front.create_text(400, 263, fill="black", text=word, font=(FONT_NAME, 35, "bold"))
#     bg_front.grid(row=0, column=0, columnspan=2, pady=20)
#
#
# bg_back_png = PhotoImage(file="images/card_back.png")
#
#
# def english_back(word):
#     bg_back = Canvas(width=800, height=526)
#     bg_back.config(bg=BACKGROUND_COLOR, highlightthickness=0)
#     bg_back.create_image(400, 263, image=bg_back_png)
#     bg_back.create_text(400, 150, fill="white", text="English", font=(FONT_NAME, 20, "italic"))
#     bg_back.create_text(400, 263, fill="white", text=word, font=(FONT_NAME, 35, "bold"))
#     bg_back.grid(row=0, column=0, columnspan=2, pady=20)
#
#
# wrong_png = PhotoImage(file="images/wrong.png")
# wrong = Button(image=wrong_png, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
# wrong.grid(row=1, column=0)
#
# right_png = PhotoImage(file="images/right.png")
# right = Button(image=right_png, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
# right.grid(row=1, column=1)
#
# next_card()
#
#
# window.mainloop()
