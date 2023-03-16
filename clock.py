from tkinter import Label, Tk
import time

def digital_clock():
    dmy=time.strftime("%d %B, %Y")
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label2.config(text=dmy)
    label.after(200, digital_clock)
    #print(app_window.geometry()) #debugging for adjusting window size and position

app_window = Tk()
app_window.title("Digital Clock")
screen_width=app_window.winfo_screenwidth()
screen_height=app_window.winfo_screenheight()
app_width=250
app_height=170
offset_width=app_width
offset_height=screen_height
app_window.geometry(f"{app_width}x{app_height}+{screen_width-offset_width}+{screen_height-offset_height}")
app_window.resizable(0,0)
app_window.configure(background='#000000')


border_width = 25

label2 = Label(app_window, font=("Segoe UI", 20), bg="#000000", fg="#ffffff", bd=border_width)
label2.grid(row=0, column=1)
label = Label(app_window, font=("Terminal", 25), bg="#000000", fg="#ffffff", bd=border_width)
label.grid(row=1, column=1)


digital_clock()
app_window.mainloop()