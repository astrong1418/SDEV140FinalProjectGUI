"""
Program: Kevin's Creamy Confections Order Processing GUI
Author: Ashley Strong
Date Last Modified: 4/15/2024
Version 1.0
This program creates a GUI for processing customer orders for the business Kevin's
Creamy Confections. It allows several options, including dine-in or take-out, cone
or sundae, and a variety of different topping selections. Then the program allows
the customer to review their order, and then submit.
"""

import tkinter as tk # import tkinter
from tkinter import ttk # import ttk for the notebook widget
from tkinter.messagebox import askokcancel, showinfo, WARNING, QUESTION # import message box and related items
from tkinter import PhotoImage # import PhotoImage for images

root = tk.Tk() # create the root, or main, window
root.title('Kevin\'s Creamy Confections') # create title of main window
root.geometry('1000x600') # set the window size
root.resizable(False, False) # window cannot be resized

filename=tk.PhotoImage(file=r"icecream3.gif") # set background image for root window
background_label = tk.Label(image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

topLabel = tk.Label(root, text="Welcome to Kevin\'s Creamy Confections!", font=('Times New Roman', 24), background="light yellow") # Creating a headline
topLabel.pack(pady=20)

label = tk.Label(root, text="Use the tabs below to navigate your order.", font=('Times New Roman', 12), background="light yellow") # create simple directions
label.pack(pady=5)

notebook = ttk.Notebook(root) # create the notebook widget
notebook.pack(pady=5, expand=True)

# creating the frames, or tabs, for the notebook widget
frame1 = tk.Frame(notebook, width=1000, height=510, background="light yellow") # Order Name, Dine-in or Take-out?
frame2 = tk.Frame(notebook, width=1000, height=510, background="light yellow") # Cone or Sundae
frame3 = tk.Frame(notebook, width=1000, height=510, background="light yellow") # Toppings
frame4 = tk.Frame(notebook, width=1000, height=510, background="light yellow") # Order Review

frame1.pack(fill='both', expand=True) # placing the frames
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

notebook.add(frame1, text='Order Name') # adding the frames to the notebook
notebook.add(frame2, text='Choose Your Treat!')
notebook.add(frame3, text='Choose Your Toppings')
notebook.add(frame4, text='Review Your Order')

# FRAME 1 ORDER NAME, DINE-IN OR TAKE-OUT

topLabel = tk.Label(frame1, text="Start Your Order Here!", font=('Times New Roman', 18), background="light yellow") # Creating a headline
topLabel.pack(pady=20)

nameVar = tk.StringVar() # naming variables for order name entry box and label widgets. This line specifically saves the order name input under variable named nameVar
custName = nameVar
nameLabel = tk.Label(frame1, text = 'Please enter a name for your order.', background="light yellow" )
nameLabel.pack(pady=20)
nameInput = tk.Entry(frame1, textvariable = nameVar)
nameInput.pack(pady=10)

# creating an askokcancel box for dinein/take out radio button
def show_selected_dineortake():
    answer = askokcancel(
        title='Continue?',
        message=f'Welcome {nameVar.get()}! You chose {selected_dineortake.get()}, is this correct?',
        icon=QUESTION)
    if answer:
        showinfo(
            title='Let\'s Create Your Treat!',
            message='Great! Create your treat on the next tab!')

# creating options for radio buttons
selected_dineortake = tk.StringVar()
items = (('Dine-in', 'Dine-In'),
         ('Take-out', 'Take-out'))

# labeling the radio button widget
label = ttk.Label(frame1, text="Dine-in or Take-out?", background="light yellow")
label.pack(pady=5)

# creating the radio buttons
for option in items:
    r = ttk.Radiobutton(
        frame1,
        text=option[0],
        value=option[1],
        variable=selected_dineortake,
    )
    r.pack(padx=50, pady=5)

# button after radio button choice
button = ttk.Button(
    frame1,
    text="Create Your Treat!",
    command=show_selected_dineortake)

button.pack(padx=5, pady=5)

# FRAME 2 CONE OR SUNDAE

topLabel = tk.Label(frame2, text="Choose Your Treat!", font=('Times New Roman', 18), background="light yellow") # Creating a headline
topLabel.pack(pady=20)

# creating options for radio buttons and setting the askokcancel message box
def show_selected_coneorsundae():
    answer = askokcancel(
        title='Continue?',
        message=f'You chose {selected_coneorsundae.get()}, is this correct?',
        icon=QUESTION)
    if answer:
        showinfo(
            title='Let\'s Choose Your Toppings!',
            message='Great! Choose your toppings on the next tab!')

selected_coneorsundae = tk.StringVar()
choices = (('Cone', 'Cone'),
         ('Sundae', 'Sundae'))

# labeling the radio button widget
label = ttk.Label(frame2, text="Would you like a cone or sundae?", background="light yellow")
label.pack(pady=5)

# creating the radio buttons
for option in choices:
    r = ttk.Radiobutton(
        frame2,
        text=option[0],
        value=option[1],
        variable=selected_coneorsundae
    )
    r.pack(padx=50, pady=5)

# button after radio button choice
button = ttk.Button(
    frame2,
    text="Choose Your Toppings!",
    command=show_selected_coneorsundae)

button.pack(padx=5, pady=5)

# FRAME 3 TOPPINGS

topLabel = tk.Label(frame3, text="Choose Your Toppings!", font=('Times New Roman', 18), background="light yellow") # Creating a headline
topLabel.pack(pady=20)

# toppings check box and related functions
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()
var9 = tk.IntVar()
toppingList = [] # defining topping list to use in askokcancel message box and order review tab
options = {}  # dictionary for the askokcancel message box
c1 = tk.Checkbutton(frame3, text='Nuts', background="light yellow",variable=var1, onvalue=1, offvalue=0)
c1.pack()
c2 = tk.Checkbutton(frame3, text='Chocolate', background="light yellow",variable=var2, onvalue=1, offvalue=0)
c2.pack()
c3 = tk.Checkbutton(frame3, text='Strawberry Syrup', background="light yellow",variable=var3, onvalue=1, offvalue=0)
c3.pack()
c4 = tk.Checkbutton(frame3, text='Pineapple Syrup', background="light yellow",variable=var4, onvalue=1, offvalue=0)
c4.pack()
c5 = tk.Checkbutton(frame3, text='Whip Cream', background="light yellow",variable=var5, onvalue=1, offvalue=0)
c5.pack()
c6 = tk.Checkbutton(frame3, text='Sprinkles', background="light yellow",variable=var6, onvalue=1, offvalue=0)
c6.pack()
c7 = tk.Checkbutton(frame3, text='Sugar Cookies', background="light yellow",variable=var7, onvalue=1, offvalue=0)
c7.pack()
c8 = tk.Checkbutton(frame3, text='Banana', background="light yellow",variable=var8, onvalue=1, offvalue=0)
c8.pack()
c9 = tk.Checkbutton(frame3, text='Maraschino Cherry', background="light yellow",variable=var9, onvalue=1, offvalue=0)
c9.pack()

def create_toppingsdict(): # create a dictionary with all available toppings options as keys, and their checkbox value as the value
    selected_toppings = tk.StringVar()
    options["Nuts"] = var1.get()
    options["Chocolate"] = var2.get()
    options["Strawberry Syrup"] = var3.get()
    options["Pineapple Syrup"] = var4.get()
    options["Whip Cream"] = var5.get()
    options["Sprinkles"] = var6.get()
    options["Sugar Cookies"] = var7.get()
    options["Banana"] = var8.get()
    options["Maraschino Cherry"] = var9.get()

def show_toppings(): # if each topping box is checked, add topping to a defined list called toppingList
    count = 0
    for key, value in options.items():
        if value == 1:
            toppingList.append(key)
    if toppingList == []:
        toppingList.append(str(None))

def show_selected_toppings(): # creating the askokcancel message box for frame 3
    create_toppingsdict()
    show_toppings()
    answer = askokcancel(
        title='Your Selected Toppings',
        message=f'You selected the following toppings, is this correct?\n{', '.join(toppingList)}', # show list of selected toppings in message box
        icon=QUESTION)
        
    if answer:
        showinfo(
            title='Let\'s Review!',
            message='Great! Let\'s review your order on the next tab!')
        command = frame_four() # This function fills in all the information in the final notebook frame, shown below
    del toppingList[:] #clear the list in case customer changes their mind, can recreate a new list of items

# button after toppings check boxes choice
button = ttk.Button(
    frame3,
    text="Review Your Order!",
    command=show_selected_toppings)

button.pack(padx=5, pady=5)


# FRAME 4 ORDER REVIEW

topLabel = ttk.Label(frame4, text="Let\'s Review Your Order!", font=('Times New Roman', 18), background="light yellow") # Creating a headline
topLabel.pack(pady=20)

separator = ttk.Separator(frame4, orient='horizontal')
separator.pack(fill='x', pady = 10)

def frame_four():
    orderLabel = ttk.Label(frame4, anchor = "center", background="light yellow", text=f'Order Name: {nameVar.get()}', font = ('Times New Roman', 14))
    orderLabel.pack(pady=5) # Line for order name
    

    dineortakeLabel = ttk.Label(frame4, anchor = "center", background="light yellow",text=f'{selected_dineortake.get()}', font = ('Times New Roman', 14))
    dineortakeLabel.pack(pady=5) # Line for dine-in or take-out

    coneorsundaeLabel = ttk.Label(frame4, anchor = "center", background="light yellow", text=f'{selected_coneorsundae.get()}', font = ('Times New Roman', 14))
    coneorsundaeLabel.pack(pady=5) # Line for cone or sundae

    toppingsLabel = ttk.Label(frame4, anchor = "center", background="light yellow", text=f'{', '.join(toppingList)}', font = ('Times New Roman', 14))
    toppingsLabel.pack(pady=5) # Line for toppings

    def show_submit(): # function for askokcancel message box after submit order button pressed
        answer = askokcancel(
        title='Submit Your Order?',
        message='Would you like to submit your order?',
        icon=QUESTION)
        if answer:
            showinfo(
                title='Your Order Has Been Submitted!',
                message='Great choice! Your order has been submitted!')
        else:
            showinfo(
                title='Start Over?',
                message='Please go back to the first tab to try again.'
            )
            destroyLabels() # destroy labels if order cancelled
            destroybutton1() # destroy submit button if order cancelled
            
    def destroyLabels(): # Function to destroy labels if order is cancelled
        orderLabel.destroy()
        dineortakeLabel.destroy()
        coneorsundaeLabel.destroy()
        toppingsLabel.destroy()


    # button to confirm and submit order
    button1 = ttk.Button(
        frame4,
        text="Submit Your Order!",
        command=show_submit)

    button1.pack(padx=5, pady=5)

    def destroybutton1(): # Function to destroy submit button if order is cancelled
        button1.destroy()

root.mainloop()



           
           