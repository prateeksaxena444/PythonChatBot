from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)



# pyttsx3
bot = ChatBot("FiinFormer")

convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by prateek',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
    'In which language you talk?',
    ' I mostly talk in english',
    'What is Equity ?',
    'Kedar is a bad bay',
    'Wassup fiini',
    'Mind your own business, you have nothing to do with what am i doing so fuck off. Go to your place and try to do something productive its fucking lockdown brooo'
]


f = open('chat.txt', 'r')
train_data = []

for line in f:
    m = re.search('(Q:|A:)?(.+)', line)
    if m:
        train_data.append(m.groups()[1].lower())


trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(train_data)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)



main = Tk()

main.geometry("800x650")

main.title("FiinFormer")
img = PhotoImage(file="bot2.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


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


answer_to_speak = "You have to ask something first";


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query.lower())
    msgs.insert(END, "\nyou : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "\nbot : " + str(answer_from_bot))
    global answer_to_speak
    answer_to_speak=answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_faq():
    query = "What is Equity ?"
    answer_from_bot = bot.get_response(query.lower())
    msgs.insert(END, "\nyou : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "\nbot : " + str(answer_from_bot))
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_btn2():
    query = "What is Fixed Income Derivative ?"
    answer_from_bot = bot.get_response(query.lower())
    msgs.insert(END, "\nyou : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "\nbot : " + str(answer_from_bot))
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_btn3():
    query = "What is Face Value ?"
    answer_from_bot = bot.get_response(query.lower())
    msgs.insert(END, "\nyou : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "\nbot : " + str(answer_from_bot))
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


def ask_from_btn4():
    query = "What is OTC ?"
    answer_from_bot = bot.get_response(query.lower())
    msgs.insert(END, "\nyou : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "\nbot : " + str(answer_from_bot))
    global answer_to_speak
    answer_to_speak = answer_from_bot
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

btn5 = Button(main, text="Speak up please", font=("Verdana", 10), command=speak)
btn5.pack(side=TOP)

sc = Scrollbar(frame)
msgs = Text(frame, width=80, height=20, yscrollcommand=sc.set, wrap=WORD)
#msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)


sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=8)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 12), command=ask_from_bot)
btn.pack()

w = Label(main, text="FAQ's :  ")
w.pack(side=LEFT)

btn1 = Button(main, text="What is Equity ?", font=("Verdana", 8), command=ask_from_faq)
btn1.pack(side=LEFT)

btn2 = Button(main, text="What is Fixed Income derivative ?", font=("Verdana", 8), command=ask_from_btn2)
btn2.pack(side=LEFT)

btn3 = Button(main, text="What is face value ?", font=("Verdana", 8), command=ask_from_btn3)
btn3.pack(side=LEFT)

btn4 = Button(main, text="What is OTC ?", font=("Verdana", 8), command=ask_from_btn4)
btn4.pack(side=LEFT)

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
