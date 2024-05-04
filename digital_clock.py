import sys
import tkinter
import time

def time_():
    now1 = time.strftime('%d %b %Y')
    now = time.strftime('%H:%M:%S')
    label1.config(text=now1,bg='blue',fg='white')
    digital_clock.config(text=now,bg='red',fg='white')
    digital_clock.after(200,time_)


main = tkinter.Tk()
main.geometry('450x200')
main.configure(bg='red')

label = tkinter.Label(main, text='Digital clock',font=('ink free', 20, 'bold'),bg='green',fg='white')
label.pack()
label1 = tkinter.Label(main, text='Digital clock',font=('ink free', 20, 'bold'))
label1.pack()
digital_clock = tkinter.Label(main,font=('ink free',40,'bold'))
digital_clock.pack(padx=10)
time_()
label = tkinter.Label(main, text='Hours         Minutes          seconds',font=('ink free',10),fg='blue')
label.pack()

main.mainloop()