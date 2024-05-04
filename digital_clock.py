import sys
import tkinter
import time

def time_():
    now = time.strftime('%H:%M:%S')
    digital_clock.config(text=now)
    digital_clock.after(200,time_)


main = tkinter.Tk()
main.geometry('450x200')

label = tkinter.Label(main, text='Digital clock',font=('ink free', 20, 'bold'))
label.pack(padx=10,pady=7)
digital_clock = tkinter.Label(main,font=('ink free',40,'bold'))
digital_clock.pack(padx=10)
time_()
label = tkinter.Label(main, text='Hours         Minutes          seconds',font=('ink free',10))
label.pack()

main.mainloop()