import tkinter as tk
import threading
import random
import keyboard

time = 0
stop_count_seconds = 0
number = 0

#shows the time
def show_time():
    global stop_count_seconds, time
    stop_count_seconds = 1
    countdown.config(
        text = "{} ms".format(time)
    )


#counts the time until pressed space
def count_seconds():
    global time, stop_count_seconds
    if stop_count_seconds == 0:
        threading.Timer(0.001, count_seconds).start()
        time = time + 1
        if keyboard.read_key() == "space":
            show_time()


#GUI for break the Countdown
def break_countdown():
    window.config(
        bg = "black",
    )
    font_size = int(min(window.winfo_screenwidth(), window.winfo_screenheight()) * 0.3 * 0.1)
    countdown.config(
        text = "you lose",
        bg = "black",
        fg = "red",
        font=("Helvetica", font_size)
    )

stop_reaction = 0 #var to stop the reaction test
#function to count random to 0 and GUI for the point you have to press space
def start_reaction():
    global number,stop_reaction

    if number == 0:
        window.config(bg = "red")
        btn_size = int(min(window.winfo_screenwidth(), window.winfo_screenheight()) * 0.3 * 0.1)
        countdown.config(
            text="Press Space!",
            bg = "red",
            fg = "white",
            font=("Helvetica", btn_size)
        )
        count_seconds()
    elif stop_reaction == 0 and number != 0:
        number = number - 1
        threading.Timer(1.0, start_reaction).start()
        if keyboard.read_key() == "space" and number != 0:
            stop_reaction = 1
            break_countdown()


#gets a random number between 1 and 3
def get_random():
    global number
    number = random.randint(1,3)
    start_reaction()

#Counts from 3 to 0
def start_countdown():
    global count
    button.destroy()

    countdown.place(
    relx=0.25,
    rely=0.25,
    relwidth=0.5,
    relheight=0.5
    )

    if count != -1:
        threading.Timer(1.0, start_countdown).start()
        countdown.config(text="{}".format(str(count)))
        count = count - 1
    else:
        get_random()

#Tkinter GUI
window = tk.Tk()
window.title("Reactiontest")
win_width= window.winfo_screenwidth()
win_height= window.winfo_screenheight()
window.geometry("%dx%d" % (win_width, win_height))
window.configure(bg="gray")

count = 3
countdown = tk.Label(
    text = count,
    foreground = "red",
    background = "gray"
    )

font_size = int(min(window.winfo_screenwidth(), window.winfo_screenheight()) * 0.5 * 0.4)
countdown.config(font=("Helvetica", font_size))


button = tk.Button(
    text = "Start",
    bg = "green",
    fg = "white",
    command = start_countdown
)

button.place(
    relx = 0.4,
    rely = 0.35,
    relwidth = 0.2,
    relheight = 0.2
)

btn_size = int(min(window.winfo_screenwidth(), window.winfo_screenheight()) * 0.5 * 0.05)
button.config(font=("Helvetica", btn_size))

window.mainloop()
