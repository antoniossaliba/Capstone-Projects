from tkinter import *
import pandas as pd
import random as rnd

random_number = 0
last_word_french = ""
last_word_english = ""

def change():
    flash_card.itemconfig(language, text="English")
    flash_card.itemconfig(word, text=globals()["last_word_english"])
    flash_card.itemconfig(language, fill="white")
    flash_card.itemconfig(word, fill="white")
def random_word_right_button():
    flash_card.itemconfig(language, fill="black")
    flash_card.itemconfig(word, fill="black")
    try:
        data = pd.read_csv("./data/words_to_learn.csv")
        french_words = data["French"].to_list()
        english_words = data["English"].to_list()
        if len(french_words) == 0 and len(english_words) == 0:
            flash_card.itemconfig(language, text="No more words to display! Congrats!")
            flash_card.itemconfig(word, text="")
            return
        if globals()["last_word_french"] != "" and globals()["last_word_english"] != "":
            french_words.remove(globals()["last_word_french"])
            english_words.remove(globals()["last_word_english"])
        globals()["random_number"] = rnd.randint(0, len(french_words) - 1)
        globals()["last_word_french"] = french_words[globals()["random_number"]]
        globals()["last_word_english"] = english_words[globals()["random_number"]]
        new_data = {"French": french_words, "English": english_words}
        data_frame = pd.DataFrame(new_data)
        data_frame.to_csv("./data/words_to_learn.csv", index=False)
    except:
        data = pd.read_csv("./data/french_words.csv")
        french_words = data["French"].to_list()
        english_words = data["English"].to_list()
        if len(french_words) == 0 and len(english_words) == 0:
            flash_card.itemconfig(language, text="No more words to display! Congrats!")
            flash_card.itemconfig(word, text="")
            return
        if globals()["last_word_french"] != "" and globals()["last_word_english"] != "":
            french_words.remove(globals()["last_word_french"])
            english_words.remove(globals()["last_word_english"])
        globals()["random_number"] = rnd.randint(0, len(english_words) - 1)
        globals()["last_word_french"] = french_words[globals()["random_number"]]
        globals()["last_word_english"] = english_words[globals()["random_number"]]
        new_data = {"French": french_words, "English": english_words}
        data_frame = pd.DataFrame(new_data)
        data_frame.to_csv("./data/words_to_learn.csv", index=False)
    flash_card.itemconfig(language, text="French")
    flash_card.itemconfig(word, text=globals()["last_word_french"])
    window.after(500, change)


def random_word_wrong_button():
    flash_card.itemconfig(language, fill="black")
    flash_card.itemconfig(word, fill="black")
    try:
        data = pd.read_csv("./data/words_to_learn.csv")
        french_words = data["French"].to_list()
        english_words = data["English"].to_list()
        if len(french_words) == 0 and len(english_words) == 0:
            flash_card.itemconfig(language, text="No more words to display! Congrats!")
            flash_card.itemconfig(word, text="")
        globals()["random_number"] = rnd.randint(0, len(french_words) - 1)
        globals()["last_word_french"] = french_words[globals()["random_number"]]
        globals()["last_word_english"] = english_words[globals()["random_number"]]
        new_data = {"French": french_words, "English": english_words}
        data_frame = pd.DataFrame(new_data)
        data_frame.to_csv("./data/words_to_learn.csv", index=False)
    except:
        data = pd.read_csv("./data/french_words.csv")
        french_words = data["French"].to_list()
        english_words = data["English"].to_list()
        globals()["random_number"] = rnd.randint(0, len(french_words) - 1)
        globals()["last_word_french"] = french_words[globals()["random_number"]]
        globals()["last_word_english"] = english_words[globals()["random_number"]]
        new_data = {"French": french_words, "English": english_words}
        data_frame = pd.DataFrame(new_data)
        data_frame.to_csv("./data/words_to_learn.csv", index=False)
    flash_card.itemconfig(language, text="French")
    flash_card.itemconfig(word, text=globals()["last_word_french"])
    window.after(500, change)

window = Tk()
window.title("Flash Card App")
window.config(width=1000, height=800, bg="#B0DB9C", pady=30)
window.minsize(1000, 800)
window.maxsize(1000, 800)

correct_button = Button(width=50, height=50, border=5, borderwidth=3, command=random_word_right_button)
img1 = PhotoImage(file="./images/right.png")
correct_button.config(image=img1)
correct_button.place(x=570, y=600)

wrong_button = Button(width=50, height=50, border=5, borderwidth=3, command=random_word_wrong_button)
img2 = PhotoImage(file="./images/wrong.png")
wrong_button.config(image=img2)
wrong_button.place(x=370, y=600)

flash_card = Canvas(width=800, height=526, border=5, bg="#B0DB9C", highlightthickness=0)
language = flash_card.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word = flash_card.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
flash_card.place(x=100, y=30)

window.mainloop()