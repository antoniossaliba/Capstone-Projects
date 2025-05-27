import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter:row.code for index, row in df.iterrows()}

user_input = input("Enter a word or (exit) to quit: ").upper()

while user_input != "EXIT":
    generated_list = [data_dict[letter] for letter in user_input]
    print(f"The generated list of words is: {generated_list}")

    user_input = input("Enter a word or (exit) to quit: ").upper()