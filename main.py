# TODO: Create a letter using starting_letter.docx

with open("Input/Names/invited_names.txt", mode="r") as names:
    clean_names = names.read()
    names_list = clean_names.split()
print(names_list)
#
with open("../MailMerge/Input/Letters/starting_letter.docx") as file:
    letter = file.read()
    for name in names_list:
        with open(f"../MailMerge/Output/ReadyToSend/letter_to_{name}.docx", mode="w") as invite:
            replace_txt = letter.replace("[name]", name)
            invite.write(replace_txt)


