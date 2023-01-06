from os import startfile
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext


# Creating the main window.
window_1 = Tk()
window_1.title("Poker Wizard v. 1.0")
window_1.geometry('245x160')
window_1.resizable(width=False, height=False)
lbl = Label(window_1)
lbl.grid(column=0, row=0)


# Function with text symbols.
def label(TEXT, X, Y, font):
    lbl = Label(window_1, text=TEXT, font=(font))
    lbl.grid(column=0, row=0)
    lbl.place(x=X, y=Y)


# Button creation function.
def button(TEXT, X, Y, com):
    btn = Button(window_1, text=TEXT, command=com)
    btn.grid(column=0, row=0)
    btn.place(x=X, y=Y)


# Message-box.
def ev_messagebox():
    messagebox.showinfo("ИНСТРУКЦИЯ", 'РАСЧЕТ EV ВЕДЕТСЯ ПО ФОРМУЛЕ:\n\
EV = ((%ВЫЙГРЫША + $ВЫЙГРЫША)-(%ПРОИГРЫША + $ПРОИГРЫША))/100\n\
РАСЧЕТ ОДДСОВ ВЕДЕТСЯ ПО ФОРМУЛЕ:\n\
ОДДСЫ=(БАНК + СТАВКА СОПЕРНИКА)/СТОИМОСТЬ КОЛЛА')


# Calculation of indicators.
def ev_calculate():
    wins_precent = txt_1.get()
    sum_wins = txt_2.get()
    sum_loses = txt_3.get()

    win_precent = int(wins_precent)
    lose_precent = 100 - int(wins_precent)
    sum_win = int(sum_wins)
    sum_lose = int(sum_loses)
    ev = ((win_precent * sum_win)-(lose_precent * sum_lose))/100

    indicator_1 = float(sum_wins) / float(sum_loses)
    indicator_2 = float(sum_loses) / float(sum_loses)
    odds = indicator_1, ":", indicator_2

    label(odds, 175, 5, font=("Arial Bold", 10, 'bold'))
    label(ev, 65, 5, font=("Arial Bold", 10, 'bold'))


# Calling buttons and text.
label("ВЭЛЬЮ:", 5, 5, font=("Arial Bold", 10, 'bold'))
label("ОДДСЫ:", 115, 5, font=("Arial Bold", 10, 'bold'))
label('% ВЫЙГРЫША:', 5, 30, font=("Arial Bold", 10))
label('СУММА ВЫЙГРЫШ:', 5, 60, font=("Arial Bold", 10))
label('СУММА ПРОИГРЫШ:', 5, 90, font=("Arial Bold", 10))
button("?", 90, 120, ev_messagebox)
button("РАСЧИТАТЬ", 5, 120, ev_calculate)

# Input fields(txt_1, txt_2, txt_3).
txt_1 = Entry(window_1, width=10)
txt_1.grid(column=0, row=0)
txt_1.place(x=155, y=30)

txt_2 = Entry(window_1, width=10)
txt_2.grid(column=0, row=0)
txt_2.place(x=155, y=60)

txt_3 = Entry(window_1, width=10)
txt_3.grid(column=0, row=0)
txt_3.place(x=155, y=90)


window_1.mainloop()