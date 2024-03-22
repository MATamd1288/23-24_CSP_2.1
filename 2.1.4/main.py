#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    if(ent_username.get() == "username" and ent_password.get() == "pass"):
        frame_auth.tkraise()
    else:
        fail_label = tk.Label(frame_login, text="Invali. Try again")
        fail_label.pack()

        frame_auth.tkraise()

# main window
root = tk.Tk()
root.wm_geometry("200x200")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()

frame_auth = tk.Frame(root)
frame_auth.grid()

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

frame_login = tk.Frame(root)
frame_login.grid()

lbl_username = tk.Label(frame_login, text='Password:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

btn_login = tk.Button(frame_login, text="login", command=test_my_button())
btn_login.pack()

frame_login.tkraise()
root.mainloop()