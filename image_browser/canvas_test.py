
from PIL import Image
from PIL import ImageTk
from tkinter import Label, Tk, Frame, Button, messagebox
import tkinter

image_list = ['1.jpg', '2.jpg', '3.jpg']
text_list = ['apple', 'bird', 'cat']
current = 0

def move(delta):
    global current, image_list
    if not (0 <= current + delta < len(image_list)):
        messagebox.showinfo('End', 'No more image.')
        return
    current += delta
    image = Image.open(image_list[current])
    photo = ImageTk.PhotoImage(image)
    label['text'] = text_list[current]
    label['image'] = photo
    label.photo = photo

root = Tk()

label = Label(root, compound=tkinter.TOP)
label.pack()

frame = Frame(root)
frame.pack()

Button(frame, text='Previous picture', command=lambda: move(-1)).pack(side=tkinter.LEFT)
Button(frame, text='Next picture', command=lambda: move(+1)).pack(side=tkinter.LEFT)
Button(frame, text='Quit', command=root.quit).pack(side=tkinter.LEFT)

move(0)
root.geometry('1400x900')
root.mainloop()
