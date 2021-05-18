import ast
from chatterbot import ChatBot
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import tkinter.messagebox
import webbrowser
from tkinter import simpledialog
import json
from functools import partial
import ctypes

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

# pyttsx3

bot = ChatBot("ASK YOTTA")

def openNewWindow():
    tkinter.messagebox.showinfo("About us","ASK YOTTA is Created by IT-Engineering and Development Team - Yotta Infrastructure Solutions")

main = Tk()

main.geometry("800x650")
main.title("ASK YOTTA")


btnabs = Button(main, text="About us", font=("Verdana", 8), bg="white", command=openNewWindow, bd="5", relief="groove")
btnabs.pack(side=TOP , anchor='w')

img = PhotoImage(file="iCON.png")

photoL = Label(main, image=img,bd="6", relief="groove")

photoL.pack(pady=5)


def getresponse(query):
    file = open("data1.json", "r")
    contents = file.read()
    d = ast.literal_eval(contents)
    file.close()
    new_d=lower_dict(d)
    query_lowercase=query.lower()
    value=''
    if value == '':
     list_ofValues=[]
     list_ofValues=list(new_d.keys())
     for key in new_d:
         if (query_lowercase in key):
                value=new_d.__getitem__(key)
                break
    return value


def lower_dict(d):
   new_dict = dict((k.lower(), v) for k, v in d.items())
   return new_dict

def speak():
    engine.say(answer_to_speak)
    engine.runAndWait()

# take query : it takes audio as input from user and convert it to string
def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(m, duration=0.2)
            audio = sr.listen(m, timeout=3, phrase_time_limit=3)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot(query)
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
        substring = answer_from_bot[startindex:]
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

def ask_from_bot(str):
    query = str
    msgs.insert(END, "\n\nyou : " + query.upper())
    answer_from_bot = getresponse(query)
    f = open('stopword.txt', 'r')
    contents_stop = f.read()
    f.close()
    if query.lower() in contents_stop:
        msgs.tag_config("noanswer", foreground="red")
        answer_from_bot="Sorry,I did not get you, please try to ask your question in other way"
        msgs.insert(END, "\n\nbot : " + str(answer_from_bot), "noanswer")
    else:
        if (answer_from_bot != ''):
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

def ask_from_bot():
    query = textF.get()
    msgs.insert(END, "\n\nyou : " + query.upper())
    answer_from_bot = getresponse(query)
    f = open('stopword.txt', 'r')
    contents_stop = f.read()
    f.close()
    if query.lower() in contents_stop:
        msgs.tag_config("noanswer", foreground="red")
        answer_from_bot="Sorry,I did not get you, please try to ask your question in other way"
        msgs.insert(END, "\n\nbot : " + str(answer_from_bot), "noanswer")
    else:
        if (answer_from_bot != ''):
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
    query = "Darwin box link"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_btn2():
    query = "Monitoring portal link"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_btn3():
    query = "Tell me about prateek saxena"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_btn4():
    query = "Prateek's Team"
    answer_from_bot = getresponse(query.lower())
    msgs.insert(END, "\n\nyou : " + query.upper())
    msgs.tag_config("answer", foreground="blue")
    handleHttp(answer_from_bot)
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)

def add_question(filename='data1.json'):
    with open('data1.json') as json_file:
        data = json.load(json_file)
        question = simpledialog.askstring(title="Question Box",
                                               prompt="Enter Question :  ")
        answer = simpledialog.askstring(title="Answer Box",
                                              prompt="Enter Answer:  ")
        temp = data
        y = {question : answer}
        temp.update(y)
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)
        ctypes.windll.user32.MessageBoxW(0, "Your question is added Successfully", "SUCCESS", 1)


frame = Frame(main)

photo = PhotoImage(file = "speakup.png")
btn5 = Button(main, text="Answer in audio format ?", font=("Verdana", 10), image=photo, command=speak)
btn5.pack(side=TOP)

voiceQuerybtn= Button(main, text="Voice call to BOT ?", font=("Verdana", 10), command=takeQuery)
voiceQuerybtn.pack(side=TOP)


add_questionBtn = Button(main, text="Add a Question", font=("Verdana", 10),command=add_question)
add_questionBtn.pack(side=TOP)

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

w = Label(main, text="FAQ's :  ", font=("Verdana", 8),bg="black", foreground="white", bd="5", relief="groove")
w.pack(side=LEFT)

btn1 = Button(main, text="Darwin box link", font=("Verdana", 8), bg="white", command=ask_from_faq, bd="5")
btn1.pack(side=LEFT)

btn2 = Button(main, text="Monitoring portal link", font=("Verdana", 8), bg="white", command=ask_from_btn2, bd="5")
btn2.pack(side=LEFT)

btn3 = Button(main, text="Tell me about prateek saxena", font=("Verdana", 8), bg="white", command=ask_from_btn3, bd="5")
btn3.pack(side=LEFT)

btn4 = Button(main, text="Prateek's Team", font=("Verdana", 8), bg="white", command=ask_from_btn4, bd="5")
btn4.pack(side=LEFT)

def callback(event):
    webbrowser.open_new("https://care.yotta.com/")


link = Label(main, text="Link to Yotta Cloud Portal", fg="dark blue", cursor="hand2", bd="5", relief="groove")
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