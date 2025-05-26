#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = []

with open("./Input/Names/invited_names.txt") as file:
    for line in file:
        names.append(line.rstrip())
print(names)
for name in names:
    with open(f"./Output/ReadyToSend/letter_to_{name}", "w") as file:
        with open(f"./Input/Letters/starting_letter.txt") as internal_file:
            letter = internal_file.read()
        letter = letter.replace("[name]", name)
        file.write(letter)