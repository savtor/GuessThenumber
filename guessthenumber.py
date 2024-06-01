import tkinter as tk
import random
window = tk.Tk()
window.geometry("900x500")
window.title("Guess The Number")
label = tk.Label(window, text="What is the number?",font=("Arial",20))
label.pack()
text = tk.Text(window,height=1,font=("Arial",20))
text.pack(padx=350)
text.config(state="normal")
text1 = text.get("1.0", "end")
guess = 0
number = 0 
button_frame = tk.Frame(window)
number1 = random.randint(1,10)
number2 = random.randint(10,100)
number3 = random.randint(100,1000)
button_frame.pack()
button_height = 5
button_width = 10 

def a1():
    global number
    number = number1
def a2():
    global number
    number  = number2
def a3():
    global number
    number  = number3

def check1():
    global number
    text2 = text.get("1.0", "end").strip()
    global guess
    if text2.isdigit():
        guess = int(text2)
        if guess == number:
            label1 = tk.Label(window, text="Correct",font=("Arial",20))
            
        elif guess == number-2 or guess == number+2 or guess == number+1 or guess == number-1:
            label1 = tk.Label(window, text="You are close",font=("Arial",20))
        else:label1 = tk.Label(window, text="Incorrect",font=("Arial",20))
        label1.pack()
        
    else: text.insert(tk.END, 'It must be a number')
def square():
    button = tk.Button(button_frame,text='Level 1',height=button_height,width=button_width,command=a1)
    button.pack(side = tk.LEFT,padx=5)
    return button
def square1():
    button1 = tk.Button(button_frame,text='Level 2',height=button_height,width=button_width,command=a2)
    button1.pack(side = tk.LEFT,padx=5)
    return button1
def square2():
    button2 = tk.Button(button_frame,text='Level 3',height=button_height,width=button_width,command=a3)
    button2.pack(side = tk.LEFT,padx=5)
    return button2

bt1 = square()
bt2 = square1()
bt3 = square2()
lv1 =  tk.Button(window,text='Submit',font=('Arial',40),command=check1 )
lv1.pack()





window.mainloop()