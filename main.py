from tkinter import *

# create window
root=Tk()

# use geometry method to create width and height of window and for distance from x and y axis
root.geometry('500x600+100+30')

# add title to window
root.title('ChatBot created by Zaina Shawar')

# add background color
# root.config(bg='lavender')
root['bg'] = '#f3c9ff'

# use the photo image class to import the image
logoPic = PhotoImage(file='logo.PNG')


# to add the image to the window add image to a label (or a button) and then place it using pack method
# pack() default puts object at top of window
logoPicLabel = Label(root, image=logoPic, bg='#f3c9ff')
logoPicLabel.pack()

# add center frame with scroll bar
centerFrame = Frame(root)
centerFrame.pack()
scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

# add text area to center frame and add scroll bar to text area
textarea = Text(centerFrame, font=('arial', 16, 'bold'), fg='#f3c9ff', height='11', width='35', bg='#8C52FF',
                yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)

# configure scroll bar buttons
scrollbar.config(command=textarea.yview)

# add entry field for question
questionField = Entry(root, font=('arial', 16, 'bold'), fg='#f3c9ff', bg='#8C52FF', width='37')
questionField.pack(pady=15)

# create ask button
askPic = PhotoImage(file='sendBtn.PNG')
askButton = Button(root, image=askPic, bg='#f3c9ff')
askButton.pack(pady='5')

# use mainloop to keep window continuously on screen
root.mainloop()


