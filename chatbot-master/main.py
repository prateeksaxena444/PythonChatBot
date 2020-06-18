import ast

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import tkinter.messagebox
import webbrowser
from PIL import ImageTk, Image
from functools import partial
from requests.structures import CaseInsensitiveDict

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)



# pyttsx3
bot = ChatBot("FiinFormer")


def openNewWindow():
    tkinter.messagebox.showinfo("About us","FiinFormer can be used to resolve your queries related to Financial Markets.Also it has features like,'listen to Bot' ,'FAQ's and 'Link to accesss Investopidia'.\n\n It is developed by a team involving 5 members: 'Aditya Thakkar, Sahim Reza, Rohit Salvi, Prateek Saxena and Vaidehi Degwekar'")

main = Tk()

main.geometry("800x650")
main.title("FiinFormer")


btnabs = Button(main, text="About us", font=("Verdana", 8), bg="light blue", command=openNewWindow, bd="5", relief="groove")
btnabs.pack(side=TOP , anchor='w')

img = PhotoImage(file="bot2.png")

photoL = Label(main, image=img, bd="6", relief="groove")

photoL.pack(pady=5)



def getresponse(query):
    file = open("data.txt", "r")
    contents = file.read()
    d = ast.literal_eval(contents)
    file.close()
    print(d)
    new_d=lower_dict(d)
    query_lowercase=query.lower()
    value=''
    print(new_d.keys())
    list_ofValues=[]
    list_ofValues=list(new_d.keys())

    for key in new_d:
         print(type(key))
         if (query_lowercase in key):
                print('yes')
                value=new_d.__getitem__(key)
                break

    return value


def lower_dict(d):
   new_dict = dict((k.lower(), v) for k, v in d.items())
   return new_dict

def speak():
    engine.say(answer_to_speak)
    engine.runAndWait()


# take query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def show_hand_cursor(b):
    msgs.config(cursor="hand2")

def hide_hand_cursor(b):
    msgs.config(cursor="")


def callbackLink(substring,tag):
    webbrowser.open(substring)

def handleHttp(answer_from_bot):
   if 'http' in answer_from_bot:
        startindex = answer_from_bot.index('http')
        print(startindex)
        substring = answer_from_bot[startindex:]
        print(substring)
        endindex = answer_from_bot.index(substring)
        msgs.insert(END, "\n\nbot : " + answer_from_bot[:endindex], "answer")
        msgs.tag_config("a", foreground="blue", underline=1)
        msgs.tag_bind("a", "<Enter>", show_hand_cursor)
        msgs.tag_bind("a", "<Leave>", hide_hand_cursor)
        msgs.tag_configure("a", foreground="blue")
        msgs.tag_bind("a", "<1>", partial(callbackLink, substring))
        msgs.insert(END, substring, "a")
   else:
        msgs.insert(END, "\n\nbot : " + str(answer_from_bot), "answer")


answer_to_speak = "You have to ask something first";


def ask_from_bot():
    query = textF.get()
    msgs.insert(END, "\n\nyou : " + query.upper())
    answer_from_bot = getresponse(query)
    print(type(answer_from_bot))
    f = open('stopword.txt', 'r')
    contents_stop = f.read()
    print(contents_stop)
    f.close()
    if query.lower() in contents_stop:
        msgs.tag_config("noanswer", foreground="red")
        answer_from_bot="Sorry,I did not get you, please try to ask your question in other way"
        msgs.insert(END, "\n\nbot : " + str(answer_from_bot), "noanswer")
    else:
        if (answer_from_bot != ''):
            #msgs.tag_config("answer", foreground="blue")
            #msgs.insert(END, "\n\nbot : " + str(answer_from_bot), "answer")
            msgs.tag_config("answer", foreground="blue")
            handleHttp(answer_from_bot)
        else:
            msgs.tag_config("noanswer", foreground="red")
            answer_from_bot = "Sorry,I did not get you, please try to ask your question in other way"
            msgs.insert(END, "\n\nbot : " + str(answer_from_bot), "noanswer")
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)

def ask_from_faq():
    query = "What is Equity?"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    print(type(answer_from_bot))
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_btn2():
    query = "What are bonds?"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    print(type(answer_from_bot))
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_btn3():
    query = "What are primary markets?"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    print(type(answer_from_bot))
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_btn4():
    query = "What is IPO?"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    print(type(answer_from_bot))
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)

def  ask_from_btn5():
    query = "Mutual fund definition"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    print(type(answer_from_bot))
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)

def  ask_from_btn6():
    query = "What are Debt Instruments?"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    print(type(answer_from_bot))
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)

def ask_from_btn7():
        query = "What is dematerialization?"
        answer_from_bot = getresponse(query.lower())
        msgs.insert(END, "\n\nyou : " + query.upper())
        print(type(answer_from_bot))
        msgs.tag_config("answer", foreground="blue")
        handleHttp(answer_from_bot)
        global answer_to_speak
        answer_to_speak = answer_from_bot
        textF.delete(0, END)
        msgs.yview(END)



frame = Frame(main)

photo = PhotoImage(file = "speakup.png")
btn5 = Button(main, text="Speak up please ?", font=("Verdana", 10), image=photo, command=speak)
btn5.pack(side=TOP)

sc = Scrollbar(frame)
msgs = Text(frame, width=170, height=18, yscrollcommand=sc.set, xscrollcommand=sc.set, wrap=WORD, background='white', bd="6",relief="ridge")
#msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)


sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=8)

frame.pack()

'''
canvas = Canvas(main, width=1000, height=100)
image = ImageTk.PhotoImage(Image.open('android.png'))

canvas.create_image(130, 0, anchor=NW, image=image)
canvas.pack()
'''

# creating text field

textF = Entry(main, font=("Verdana", 20), background="white", bd="6", relief="ridge")
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask the Bot", fg="dark blue", font=("Verdana", 12), bd= "4", command=ask_from_bot)
btn.pack()

w = Label(main, text="FAQ's :  ", font=("Verdana", 8), bg="dark blue", foreground="white", bd="5", relief="groove")
w.pack(side=LEFT)

btn1 = Button(main, text="What is Equity ?", font=("Verdana", 8), bg="light blue", command=ask_from_faq, bd="5")
btn1.pack(side=LEFT)

btn2 = Button(main, text="What are bonds?", font=("Verdana", 8), bg="light blue", command=ask_from_btn2, bd="5")
btn2.pack(side=LEFT)

btn3 = Button(main, text="What are primary markets?", font=("Verdana", 8), bg="light blue", command=ask_from_btn3, bd="5")
btn3.pack(side=LEFT)

btn4 = Button(main, text="What is IPO?", font=("Verdana", 8), bg="light blue", command=ask_from_btn4, bd="5")
btn4.pack(side=LEFT)

btn5 = Button(main, text="Mutual fund definition", font=("Verdana", 8), bg="light blue", command=ask_from_btn5, bd="5")
btn5.pack(side=LEFT)

btn6 = Button(main, text="What are Debt Instruments?", font=("Verdana", 8), bg="light blue", command=ask_from_btn6, bd="5")
btn6.pack(side=LEFT)

btn7 = Button(main, text="What is dematerialization?", font=("Verdana", 8), bg="light blue", command=ask_from_btn7, bd="5")
btn7.pack(side=LEFT)

def callback(event):
    webbrowser.open_new(r"http://www.investopedia.com/")


link = Label(main, text="Link to Investopedia", fg="dark blue", cursor="hand2", bd="5", relief="groove")
link.pack(side=RIGHT,anchor='e')
link.bind("<Button-1>", callback)





# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()