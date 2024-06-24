import tkinter as tk
from timeit import default_timer as tim
import random

def test():
    
    info1=e1.get()
    if info1==sentence:
        end=tim()
        l2.config(text=f'Time required : {(end-start)}s')   
    else:
        l2.config(text="Wrong input")   


root=tk.Tk()
root.title("Typing Speed Test")
root.minsize(width=400,height=400)
root.geometry("600x400")

sentences = ['Hello, this a python program.',
       'This program calculates the time required to type a sentence.',
       'It returns time in seconds.',
       'How much time do you require to type this sentence?']
        
sentence = random.choice(sentences)

start=tim()
lbl=tk.Label(root,text="Welcome to Typing Speed Test. Start typing")
lbl.pack(pady=20)

sentence_label=tk.Label(root,text=sentence,font=20)
sentence_label.pack(pady=40)

l1=tk.Label(root, text="Enter text")
l1.pack()

e1=tk.Entry(root,width=400)
e1.pack()

b1=tk.Button(root, text="Done",command=test)
b1.pack()

l2=tk.Label(root)
l2.pack()

b2=tk.Button(root,text="Exit",command=root.destroy)
b2.pack()
root.mainloop()
