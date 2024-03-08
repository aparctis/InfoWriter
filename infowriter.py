from tkinter import *
from tkinter import ttk 
import postwriter

root = Tk()


#INTERFACE
root['bg'] = '#8feaf7'
root.title('Letter writer')
root.geometry('900x650')
root.resizable(width=False, height=False)


#FRAMES
frame_top_center = Frame(root, bg='#1177e7', bd=5)
frame_top_center.place(relx=0.15, rely=0.025, relwidth=0.7, relheight=0.2)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.85)


#LETTER TEXT
letterInfo = Label(frame_bottom, wraplength=700, text='Лист', bg='#ffb700', font=("Arial", 7))
letterInfo.pack()

#LETTER BUTTON FUNCTIONS
def create_text():
	global activeManager
	letter_text = postText
	letterInfo['text'] = postwriter.maintext
	pyperclip.copy(letter_text)

#LETTER BUTTONS
btnLinkedin1 = Button(frame_top_center, text='Створити текст поста', command=create_text)
btnLinkedin1.pack(anchor=NW)

root.mainloop()