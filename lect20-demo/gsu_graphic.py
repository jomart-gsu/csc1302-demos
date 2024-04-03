from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT
root = Tk()
#transform the GIF image to a format tkinter can display
photo1 = PhotoImage(file='gsu-logo.gif')
photo2 = PhotoImage(file='mascot.gif')
logo = Label(root, image=photo1, width=300, height=300)
mascot = Label(root, image=photo2, width=300, height=300)
text = Label(
    root,
    font=('Helvetica', 16, 'bold italic'),
    foreground='white',
    background='blue',
    padx=25, pady=10,
    text='Georgia State University'
)
text.pack(side=BOTTOM)
logo.pack(side=LEFT)
mascot.pack(side=RIGHT)
root.mainloop()