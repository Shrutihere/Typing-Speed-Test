from tkinter import *
import random

DATA = [''' this meant most people were somewhat slow in investing in stocks and bonds because these securities could not readily be converted into money. we have been told that an interesting number of traders and merchants agreed to try to do something to helpcorrect the situation. at this first crucial meeting, they decided that it was a good idea to visit regularly on a daily basis to buy and sell securities.the group of   leaders, whose meeting place was under an old, tall cotton not to use too many difficult words in it although i think that i might start making''',
             ''' this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of run on sentences this should help you get faster at typing as im trying not to use too many difficult words in it although i think that i might start making it hard by including some more difficult letters I'm typing pretty quickly so forgive me for any mistakes i think that i will not just tell you a story about the time i went to the zoo and found a''',
             ''' typing is quite easy and enjoyable when you have learned to do it correctly. it is amazing just how quick you can be when you learn to touch type all the letters exactly, from a to z. just relax and realize that typing with excellent accuracy is far better than typing fast; you will find it is quicker in the end on the door there is someone i want to run away to another galaxy but that is not possible so i am here feeling lonely this is going quite alright keep it up  typing is a physical skill, and the only way to improve is to practice regularly.''',
             ''' these paragraph based typing tests contain longer text passages on a variety of subjects. choose a topic below. we have a large variety of typing practice with texts from a number of areas of interest to stimulate your mind while exercising your fingers. if you are preparing for a specific career field like medicine or technology then you may also find those subjects useful in learning vocabulary and gaining muscle memory for the jargon particular to the kind of job you have, or hope to get your stamina so that you can easily maintain your maximum speed''',
             ''' to get the best scores on these practice typing tests, try to relax and focus on your accuracy. all of our drills require 100% accuracy before they give you a score. you can correct your mistakes as you go by using the backspace key, or wait until the end and use the spell checker features. most pre-employment typing test are given in this format and last for approximately 5 minutes. if you are anxious about an upcoming typing test, try to practice typing for at least 10 minutes a day to build up  and accuracy for the entire test.''']
PARAGRAPH = random.choice(DATA)
counter=1
TIME=60
score = 0
user_can_type = True

# --------UNDO FOR BACKSPACE--------

def backspace(event):
    global counter
    counter -= 1
    para.tag_remove("start", f"1.{counter}", f"1.{counter + 1}")
    para.tag_remove("mistake", f"1.{counter}", f"1.{counter + 1}")


# --------START COUNTDOWN--------

def start_timer(t):
    global user_can_type
    if t >= 0:
        timer.config(text=f"Time: {t} sec")
        window.after(1000, start_timer, t-1)
    else:
        user_can_type = False
        text_input.config(state="disable")
        input_label.config(text=f"Your speed : {score} WPS")


# ---------CHECK USER INPUT KEY--------

def key_press(event):
    global counter, score, user_can_type, TIME
    if counter == 1:
        start_timer(TIME)
    key = event.char
    letter = PARAGRAPH[counter]
    if user_can_type:
        if key == letter:
            para.tag_add("start", f"1.{counter}", f"1.{counter+1}")
            para.tag_config("start", background="#4a1c40",
                            foreground="#fff5b7")
            if letter == " ":
                score += 1
        else:
            para.tag_add("mistake", f"1.{counter}", f"1.{counter + 1}")
            para.tag_config("mistake", background="red",
                            foreground="#fff5b7")
        counter += 1


# --------UI SET-UP --------

window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady= 100, bg="#fff5b7" )
window.geometry("1500x1000")

title = Label(text="---TYPING SPEED TEST---", font = "Times 40", bg="#fff5b7")
title.grid(row=0, column=0)

para = Text(font="Times 22", bg="#f6dfeb", height=6, padx=20, pady=20)
para.insert(INSERT, PARAGRAPH)
para.insert(END, " ")
para.grid(row=1, column=0, padx=20, pady=20 )

input_label = Label(text="Start Typing Below", font = "Times 30", bg="#fff5b7" )
input_label.grid(row=2, column=0, padx= 20, pady=0,)

text_input = Entry(window, font = "Times 30",)
text_input.grid(row=3, column=0, padx= 45, pady=20, ipadx=50, ipady=20)
text_input.focus()

timer = Label(text="Time: 60 sec", font = "Times 30", bg="#fff5b7")
timer.grid(row=4, column=0)

# --------BINDING FUNCIONS--------

text_input.bind('<Key>', key_press)
text_input.bind('<BackSpace>', backspace)

window.mainloop()

print("Score:",score)

