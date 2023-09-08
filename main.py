import customtkinter as ctk
from tkinter import *


# Initializing the app
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


# global var
c_radius, mid  = 10, 0.5
pad_x, pad_y = 10, 10
widthx, heighty = 170, 35

prompt = """
    Choose a Language
"""


# Root window
root = ctk.CTk()
root.geometry("600x520")
root.title("Helium Notes")

# Initializing the frame
frame = ctk.CTkFrame(master = root, width = 590, height = 510, corner_radius = c_radius)

text_box = ctk.CTkTextbox(master = frame, width = widthx, height = 70,
                          corner_radius = c_radius, bg_color = "black", fg_color = "yellow")

text_box.insert(0.0, text = prompt)


# check boxes
python = ctk.CTkCheckBox (master = frame, corner_radius = 3, text = "Python")
java   = ctk.CTkCheckBox (master = frame, corner_radius = 3, text = "Java")
go     = ctk.CTkCheckBox (master = frame, corner_radius = 3, text = "Go")

var_text = StringVar (value=" ")

# log callback
def log():
    txt1 = " "

    if python.get():
        txt1 = "Python"
        var_text.set(txt1)
    if java.get():
        txt1 = f"{txt1} Java"
        var_text.set ( txt1 )
    if go.get():
        txt1 = f"{txt1} Go"
        var_text.set ( txt1 )


# Button
show_btn = ctk.CTkButton (master = frame, text = "Reveal Choice", corner_radius = c_radius, command = log)

# Label

msg_box = ctk.CTkLabel (master = frame, textvariable = var_text, width = widthx, height = heighty, bg_color = "black", fg_color = "white")


frame.pack(padx = pad_x, pady = pad_y)
text_box.place(relx = mid, rely = 0.2, anchor = CENTER)
python.place(relx = mid, rely = 0.4, anchor = CENTER)
java.place(relx=mid, rely=0.5, anchor = CENTER)
go.place(relx=mid, rely = 0.6, anchor = CENTER)
show_btn.place(relx=mid, rely=0.7, anchor = CENTER)
msg_box.place(relx=mid, rely=0.8, anchor = CENTER)


if __name__ == '__main__':
    root.mainloop ()
