from tkinter import *
from random import randint

root = Tk()
root.title('It would be great if you learn portuguese before going to Portugal ')

root.geometry("550x410")

words = [

    (("adeus"),          ("goodbye")),
    (("amanhã"),         ("tomorrow")),
    (("amor"),           ("love")),
    (("bom"),            ("good")),
    (("cão"),            ("dog")),
    (("fazer"),          ("make")),
    (("gato"),           ("cat")),
    (("hoje"),           ("today")),
    (("hora"),           ("hour")),
    (("loga"),           ("shop")),
    (("longe"),          ("far")),
    (("mau"),            ("bad")),
    (("minuto"),         ("minute")),
    (("não"),            ("no")),
    (("obrigado"),       ("thank you")),
    (("como está?"),     ("how are you?")),
    (("olá"),            ("hello")),
    (("tudo bem"),       ("everything is fine")),
    (("bem"),            ("fine")),
    (("tudo"),           ("everything")),
    (("mais"),           ("more")),
    (("ou"),             ("or")),
    (("pare"),           ("stop")),
    (("como se chama?"), ("what is your name?")),
    (("de nada"),        ("you are welcome")),
    (("meu nome é"),     ("my name is")),
    (("desculpe"),       ("i am sorry"))

]

count = len(words)

def next():
    global hinter, hint_count
    #Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    #Reset Hint things
    hint_label.config(text="")
    hinter = ""
    hint_count = 0
    #Create random selection
    global random_word
    random_word = randint(0, count-1)
    #Portguese Word
    portuguese_word.config(text=words[random_word][0])


def answer():
    if my_entry.get() == words[random_word][1]:
        answer_label.config(text="Correct")
    else:
        answer_label.config(text="Incorrect!")

#track the hints
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count +=1

portuguese_word = Label(root, text="", font=("Helvetica", 36))
portuguese_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1, padx=20)

hint_button = Button(button_frame, text="Hint", command= hint)
hint_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)


# Run next function when program starts
next()





root.mainloop()
