import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./Small-Apps/Flash Cards/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./Small-Apps/Flash Cards/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
# except IndexError:
#     original_data = pandas.read_csv("data/french_words.csv")
#     to_learn = original_data.to_dict(orient="records")
# except:
#     original_data = pandas.read_csv("data/french_words.csv")
#     to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ------------NEXT FLASHCARD----------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card['French']
    french_front(french_word)

    print(len(to_learn))
    to_learn.remove(current_card)
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("./Small-Apps/Flash Cards/data/words_to_learn.csv", index=False)

    flip_timer = window.after(3000, flip_card)


#-------------FLIP FLASHCARD----------#
def flip_card():
    global current_card
    english_word = current_card['English']
    english_back(english_word)


#------------RE-INCLUDING UNKNOWN WORDS-------------#
def mistakes():
    global current_card
    to_learn.append(current_card)
    next_card()


#------------UI DESIGN---------------#
window = Tk()
window.title("Frenchly")
window.config(bg=BACKGROUND_COLOR, padx=80, pady=50)

bg_front_png = PhotoImage(file="./Small-Apps/Flash Cards/images/card_front.png")


def french_front(word):
    bg_front = Canvas(width=800, height=526)
    bg_front.create_image(400, 263, image=bg_front_png)
    bg_front.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    card_title = bg_front.create_text(400, 150, fill="black", text="French", font=(FONT_NAME, 20, "italic"))
    card_word = bg_front.create_text(400, 263, fill="black", text=word, font=(FONT_NAME, 35, "bold"))
    bg_front.grid(row=0, column=0, columnspan=2, pady=20)


bg_back_png = PhotoImage(file="./Small-Apps/Flash Cards/images/card_back.png")


def english_back(word):
    bg_back = Canvas(width=800, height=526)
    bg_back.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    bg_back.create_image(400, 263, image=bg_back_png)
    bg_back.create_text(400, 150, fill="white", text="English", font=(FONT_NAME, 20, "italic"))
    bg_back.create_text(400, 263, fill="white", text=word, font=(FONT_NAME, 35, "bold"))
    bg_back.grid(row=0, column=0, columnspan=2, pady=20)


wrong_png = PhotoImage(file="./Small-Apps/Flash Cards/images/wrong.png")
wrong = Button(image=wrong_png, bg=BACKGROUND_COLOR, highlightthickness=0, command=mistakes)
wrong.grid(row=1, column=0)

right_png = PhotoImage(file="./Small-Apps/Flash Cards/images/right.png")
right = Button(image=right_png, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
