import hashlib 
from tkinter import *
from firebase import firebase

registration_window = Tk()
registration_window.geometry("400x400")
registration_window.configure(background = "Green")
firebase = firebase.FirebaseApplication("https://encryptedchat-d15f0-default-rtdb.firebaseio.com/", None)



def login(): 
    print("Login Funtion")
    
def register(): 
    username = username_entry.get()
    password = password_entry.get()
    encrypted_password = hashlib.md5(password)
    hexiencrypted_password = encrypted_password.hexdigest()
    print(hexiencrypted_password)
    firebase.put( "/", username, password)
    messagebox.showinfo("Registered", "User is Registered")
    
def login_window():
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.configure(background = "Green")
    global login_username_entry
    global login_password_entry
    registration_window.destroy()
    
    login_username_entry = []
    login_password_entry = []
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold', bg = "Green")
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13',bg = "Green")
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13')
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT, bg = "Green", fg = "Black")
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold', bg = "Green")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13', bg = "Green")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13', bg = "Green")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10, bg = "Green", fg = "Black")
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT, bg = "Green", fg = "Black")

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()