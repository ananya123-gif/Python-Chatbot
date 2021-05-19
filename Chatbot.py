from tkinter import*
import pyttsx3 as pp
import speech_recognition as s
import threading
import parser
from math import factorial
import random
import wolframalpha
import wikipedia
import time
from PIL import ImageTk, Image
import calendar
i = 0


def calculator():
    root = Tk()
    root.title("Calculator")
    root.geometry("360x230")
    root.config(bg='#faa21f')

    def get_variables(num):
        global i
        display.insert(i, num)
        i += 1

    def get_operation(operator):
        global i
        length = len(operator)
        display.insert(i, operator)
        i += length

    def clear_all():
        display.delete(0, END)

    def undo():
        entire_string = display.get()
        if len(entire_string):
            new_string = entire_string[:-1]
            clear_all()
            display.insert(0, new_string)
        else:
            clear_all()
            display.insert(0, "Error")

    def calculate():
        entire_string = display.get()
        try:
            a = parser.expr(entire_string).compile()
            result = eval(a)
            clear_all()
            display.insert(0, result)
        except Exception:
            clear_all()
            display.insert(0, "Error")

    def fact():
        entire_string = display.get()
        try:
            result = factorial(int(entire_string))
            clear_all()
            display.insert(0, result)
        except Exception:
            clear_all()
            display.insert(0, "Error")

    # adding the input field

    display = Entry(root, width=50, justify="right", bd=0, bg="light blue")
    display.grid(row=1, columnspan=6, sticky=N + E + W + S)
    # Code to add buttons to the Calculator
    Button(root, text="1", command=lambda: get_variables(1), height=2, width=7, bg='#faa21f').grid(row=2, column=0,
                                                                                      sticky=N + S + E + W)
    Button(root, text=" 2", command=lambda: get_variables(2), height=2, width=7, bg='#faa21f').grid(row=2, column=1,
                                                                                      sticky=N + S + E + W)
    Button(root, text=" 3", command=lambda: get_variables(3), height=2, width=7, bg='#faa21f').grid(row=2, column=2,
                                                                                      sticky=N + S + E + W)

    Button(root, text="4", command=lambda: get_variables(4), height=2, width=7, bg='#faa21f').grid(row=3, column=0,
                                                                                     sticky=N + S + E + W)
    Button(root, text=" 5", command=lambda: get_variables(5), height=2, width=7, bg='#faa21f').grid(row=3, column=1,
                                                                                      sticky=N + S + E + W)
    Button(root, text=" 6", command=lambda: get_variables(6), height=2, width=7, bg='#faa21f').grid(row=3, column=2,
                                                                                      sticky=N + S + E + W)

    Button(root, text="7", command=lambda: get_variables(7), height=2, width=7,bg='#faa21f').grid(row=4, column=0,
                                                                                     sticky=N + S + E + W)
    Button(root, text=" 8", command=lambda: get_variables(8), height=2, width=7, bg='#faa21f').grid(row=4, column=1,
                                                                                      sticky=N + S + E + W)
    Button(root, text=" 9", command=lambda: get_variables(9), height=2, width=7, bg='#faa21f').grid(row=4, column=2,
                                                                                      sticky=N + S + E + W)

    # adding other buttons to the calculator
    Button(root, text="AC", command=lambda: clear_all(), height=2, width=7, bg='#faa21f').grid(row=5, column=0, sticky=N + S + E + W)
    Button(root, text=" 0", command=lambda: get_variables(0), height=2, width=7, bg='#faa21f').grid(row=5, column=1,    sticky=N + S + E + W)
    Button(root, text=" .", command=lambda: get_variables("."), height=2, width=7, bg='#faa21f').grid(row=5, column=2,
                                                                                        sticky=N + S + E + W)

    Button(root, text="+", command=lambda: get_operation("+"), height=2, width=7, bg='#faa21f').grid(row=2, column=3,
                                                                                       sticky=N + S + E + W)
    Button(root, text="-", command=lambda: get_operation("-"), height=2, width=7, bg='#faa21f').grid(row=3, column=3,
                                                                                       sticky=N + S + E + W)
    Button(root, text="", command=lambda: get_operation(""), height=2, width=7, bg='#faa21f').grid(row=4, column=3,
                                                                                       sticky=N + S + E + W)
    Button(root, text="/", command=lambda: get_operation("/"), height=2, width=7, bg='#faa21f').grid(row=5, column=3,
                                                                                       sticky=N + S + E + W)

    # adding new operations
    Button(root, text="pi", command=lambda: get_operation("*3.14"), height=2, width=7, bg='#faa21f').grid(row=2, column=4,
                                                                                            sticky=N + S + E + W)
    Button(root, text="%", command=lambda: get_operation("%"), height=2, width=7, bg='#faa21f').grid(row=3, column=4,
                                                                                       sticky=N + S + E + W)
    Button(root, text="(", command=lambda: get_operation("("), height=2, width=7, bg='#faa21f').grid(row=4, column=4,
                                                                                       sticky=N + S + E + W)
    Button(root, text="exp", command=lambda: get_operation("**"), height=2, width=7, bg='#faa21f').grid(row=5, column=4,
                                                                                          sticky=N + S + E + W)

    Button(root, text="<-", command=lambda: undo(), height=2, width=7, bg='#faa21f').grid(row=2, column=5, sticky=N + S + E + W)
    Button(root, text="x!", command=lambda: fact(), height=2, width=7, bg='#faa21f').grid(row=3, column=5, sticky=N + S + E + W)
    Button(root, text=")", command=lambda: get_operation(")"), height=2, width=7, bg='#faa21f').grid(row=4, column=5,
                                                                                       sticky=N + S + E + W)
    Button(root, text="^2", command=lambda: get_operation("**2"), height=2, width=7, bg='#faa21f').grid(row=5, column=5,
                                                                                          sticky=N + S + E + W)
    Button(root, text="^2", command=lambda: get_operation("**2"), height=2, width=7, bg='#faa21f').grid(row=5, column=5,
                                                                                          sticky=N + S + E + W)
    Button(root, text="=", command=lambda: calculate(), height=2, width=7, bg='#faa21f').grid(columnspan=6, sticky=N + S + E + W)

    root.mainloop()
# Function for showing the calendar of the given year


def Calendar():
    def showCal():
        root1 = Tk()
        root1.config(bg='#faa21f')
        root1.title("MY CALENDAR")
        root1.geometry("520x600")
        fetch_year = int(year_field.get())
        cal_data = calendar.calendar(fetch_year)
        cal_year = Label(root1, text=cal_data, font="Lucida 10 bold", bg='#faa21f')
        cal_year.grid(row=7, column=1, padx=20,)
        root1.mainloop()

    if __name__ == '__main__':
        gui = Tk()
        gui.config(bg='#faa21f')
        gui.title("CALENDAR")
        gui.geometry("200x200")
        cal = Label(gui, text="CALENDAR", bg="red", font="Vardana 26 bold")
        year = Label(gui, text="Enter Year", bg="light green", font="Vardana 12 bold")
        year_field = Entry(gui)
        Show = Button(gui, text="Show Calendar", fg="Black",bg="Red", font="Vardana 10 bold", command=showCal)
        Exit = Button(gui, text="Exit", bg="Red", font="Vardana 10 bold", command=exit)
        cal.grid(row=1, column=1)
        year.grid(row=2, column=1)
        year_field.grid(row=3, column=1)
        Show.grid(row=4, column=1)
        Exit.grid(row=6, column=1)
        gui.mainloop()


# pyttsx3
engine = pp.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 120)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# take query: it takes audio from the user and convert into string
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')  # convert audio to string after listening from microphone as m
            print(query)
            entry.configure(state=NORMAL)
            entry.insert('1.0', query)  # insert your audio on text field too
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")

# Function to search the query
# that is either entered or spoken
# by user


def ask_from_bot():
   InsEntry = entry.get('1.0', 'end-1c')
   entry.configure(state=NORMAL)
   global label_request
   label_request = Label(frame_chats, text=InsEntry, bg='#faa21f', fg='#1e282d', justify=LEFT, wraplength=300,
                         font='Verdana 10 bold')

   label_request.pack(anchor='e')
   entry.delete('1.0', END)


# try is used for searching with wolframAlpha
   try:
           if InsEntry == "hello" or InsEntry == "hi" or InsEntry == "hey":
                   Response = ["hello", "hii"]
                   RandRes = random.choice(Response)
                   # to open the state of textarea to write
                   entry.configure(state=NORMAL)
                   label_response = Label(frame_chats, text=RandRes, bg='#577e75', fg='#faa21f', justify=LEFT,
                                      wraplength=300,
                                      font='Verdana 10 bold')

                   label_response.pack(anchor='w')
                   speak(RandRes)
           elif InsEntry == "good morning" or InsEntry == "morning":
                   Response = ["morning", "good morning"]
                   RandRes = random.choice(Response)
                   entry.configure(state=NORMAL)
                   label_response = Label(frame_chats, text=RandRes, bg='#577e75', fg='#faa21f', justify=LEFT,
                                          wraplength=300,
                                          font='Verdana 10 bold')

                   label_response.pack(anchor='w')
                   speak(RandRes)

           elif InsEntry == "what is your name" or InsEntry == "what is your name?":
                   Response = "My name is Chatbot."
                   entry.configure(state=NORMAL)
                   label_response = Label(frame_chats, text=Response, bg='#577e75', fg='#faa21f', justify=LEFT,
                                          wraplength=300,
                                          font='Verdana 10 bold')

                   label_response.pack(anchor='w')
                   speak(Response)
           elif InsEntry == 'Bye':
                   main.destroy()
           else:
                   # Generate your App ID from WolframAlpha
                   app_id = "39K2LE-EJLP76P4P6"
                   client = wolframalpha.Client(app_id)
                   res = client.query(InsEntry)
                   answer = next(res.results).text
                   print(answer)
                   # to open the state of textarea to write
                   entry.configure(state=NORMAL)
                   label_response = Label(frame_chats, text=answer, bg='#577e75', fg='#faa21f', justify=LEFT, wraplength=300,
                              font='Verdana 10 bold')

                   label_response.pack(anchor='w')
                   speak(answer)
                   if answer == 'Bye':
                       main.destroy()

    # If the query cannot be searched using
    # WolframAlpha then it is searched in
    # wikipedia
   except:

        answer = wikipedia.summary(InsEntry,  sentences=2)
        print(wikipedia.summary(InsEntry, sentences=2))
        # to open the state of textarea to write
        entry.configure(state=NORMAL)
        label_response = Label(frame_chats, text=answer, bg='#577e75', fg='#faa21f', justify=LEFT, wraplength=300,
                               font='Verdana 10 bold')

        label_response.pack(anchor='w')
        speak(answer)
        if answer == 'Bye':
           main.destroy()


def refresh_screen():
   for widget in frame_chats.winfo_children():
        widget.destroy()

   frame_chats.pack()
   label_space = Label(frame_chats, bg='#263238', text='')
   label_space.pack()


def welcome_to_chat():
    frame_welcome.pack_forget()
    frame_chat.pack()


def chat_to_welcome():
    frame_chat.pack_forget()
    frame_welcome.pack()


if __name__ == '__main__':
    main = Tk()

"""     WELCOME FRAME    """
"""    first frame containing time date and welcome messages """
frame_welcome = Frame(main, bg='#263238', height='650', width='550')
frame_welcome.pack_propagate(0)
frame_welcome.pack()

name = Label(frame_welcome, text='*MyChatBot*', font="Vardana 20 bold", bg='#263238', fg="white")
name.pack()

frame_spacer = Frame(frame_welcome, bg='#faa21f', height="5", width="550")
frame_spacer.pack()
frame_spacer.place(x=0,y=150)

welcome = Label(frame_welcome, text='WELCOME', font="Vardana 40 bold", bg='#263238', fg="white")
welcome.place(x=160, y=170)

welcome_chatbot = Label(frame_welcome, text='I am Chatbot! ', font="Helvetica 15 bold italic", bg='#263238', fg='#577e75')
welcome_chatbot.place(x=230, y=240)

img = Image.open("chatbot4.png")
img = img.resize((450, 510), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
photoL = Label(frame_welcome, image=img)
photoL.place(x=40, y=280)

front = ImageTk.PhotoImage(Image.open("arrow_ahead.png"))
button_front = Button(frame_welcome, image=front, relief="flat", bg='#263238', bd="3px solid black",
                      command=welcome_to_chat).place(x=470, y=63)

"""  time option  """


def clock():
    current = time.strftime("%H:%M:%S")
    label_time = Label(frame_welcome, bd=5, text=current, height=1, width=8, font='Ariel 11 bold', fg="white",
                       relief='groove', bg='#1e282d')
    label_time.place(x=120, y=63)
    label_time.after(1000, clock)


button_time = Button(frame_welcome, text='Time', height=1, font='Vardana 10 bold', width=8, bg='#faa21f', fg='#263238', command=clock)
button_time.place(x=30, y=63)
"""    date option   """


def date():
    try:
        date = time.strftime("%d %B , 20%y")
        label_date = Label(frame_welcome, bd=5, relief='groove', text=date, bg='#1e282d', fg="white", height=1,
                           font='Ariel 11 bold')
        label_date.place(x=120, y=103)

        label_date.after(86400000, date)
    except AttributeError:
        print('')


button_date = Button(frame_welcome, text='Date', height=1, font='Vardana 10 bold', width=8, bg='#faa21f', fg='#263238', command=date)
button_date.place(x=30, y=103)

"""         CHAT FRAME   """
""""       main chat screen   """
frame_chat = Frame(main, bg='#263238', height='650', width='550')
frame_chat.pack_propagate(0)

name1 = Label(frame_chat, text="*MyChatBot*", font="Vardana 20 bold", bg='#263238', fg="white")
name1.pack()

heading = Label(frame_chat, text="Hello! How can I help you?", bg='#263238', fg='white', font='Verdana 10 bold ')
heading.pack()

frame_spacer = Frame(frame_chat, bg='#faa21f', height="10", width="550")
frame_spacer.pack()

bottom_frame = Frame(frame_chat, bg='#faa21f', height='100', width='550')
bottom_frame.pack_propagate(0)
bottom_frame.pack(side=BOTTOM)

button = Button(bottom_frame, text="AskFromBot", font='Vardana 10 bold', bg='#263238',fg='#faa21f',activebackground="light blue", command=ask_from_bot)
button.place(x=410, y=27)

entry = Text(bottom_frame, bg='#263238', fg='#577e75', height='5', width='45', font='Verdana 10')
entry.place(x=30, y=10)

frame_chats = Frame(frame_chat, bg='#263238', height='450', width='450')
frame_chats.pack_propagate(0)
frame_chats.pack()

button_calculator = Button(frame_chat, bg='#263238', fg='#faa21f', text='Calculator', font='Vardana 10 bold', command=calculator)
button_calculator.place(x=120, y=520)

button_calendar = Button(frame_chat, bg='#263238', fg='#faa21f', text='Calendar', font='Vardana 10 bold', command=Calendar)
button_calendar.place(x=250, y=520)

label_space = Label(frame_chats, bg='#263238').pack()

button_refresh = Button(bottom_frame, bg='#263238', fg='#faa21f', text='refresh', font='Vardana 10 bold', command=refresh_screen)
button_refresh.place(x=430, y=57)

back = ImageTk.PhotoImage(Image.open("arrow_behind.png"))
button_back = Button(frame_chat, image=back, relief="flat", bg='#263238', command=chat_to_welcome).place(x=10, y=30)
exitt = ImageTk.PhotoImage(Image.open("exit.png"))
button_exit = Button(frame_chat, image=exitt, relief="flat", bg='#263238', command=main.destroy).place(x=500, y=20)


# creating a function
def enter_function(event):
    button.invoke()


# going to bind window with enter key...
entry.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)
t.start()

main.mainloop()
