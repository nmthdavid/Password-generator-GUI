from tkinter import *
import random

def agree():
    global nums
    if(x.get()==1):
        nums = False
    else:
        nums = True
        print("Include")

def generate():
    global nums
    global password1
    global password2
    password1 = ""
    password2 = ""
    if nums == False:
        for i in range(10):
            password1=password1+str(random.choice(abc))

        passwordLabel.config(text=password1)

    else:
        for i in range(10):
            password2=password2+str(random.choice(all))

        passwordLabel.config(text=password2)

window = Tk()

window.title("Password Generator")
appName = Label(window, text= "Password Generator", font =("Arial",30))
appName.grid(row=0,column=0,columnspan=3)

x = IntVar()
checkbox = Checkbutton(window,
                       text = "Do not include numbers",
                       variable = x,
                       onvalue = 1,
                       offvalue= 0,
                       command = agree,
                       compound = "right")
checkbox.grid(row=1,column=0)

submitButton = Button(window,text="Generate",command=generate)
submitButton.grid(row=1,column=1,columnspan=2)

passwordLabel = Label(window,text="Your Password",font =("Arial",20))
passwordLabel.grid(row=2,column=0,columnspan=3)

nums = [0,1,2,3,4,5,6,7,8,9]
alphabet = ["q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m"]
ALPHABET = []
for i in range(len(alphabet)):
    ALPHABET.append(alphabet[i].upper())

abc = alphabet+ALPHABET
all=alphabet+ALPHABET+nums

window.mainloop()
