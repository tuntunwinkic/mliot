# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *
from fastai.vision import *
from picamera import PiCamera
camera = PiCamera()

path = Path()
model = load_learner(path,'export.pkl')
# globally declare the expression variable 
expression = "" 

readvar=100
# Function to update expressiom 
# in the text entry box 
def press(num): 
	# point out the global expression variable 
	global expression 

	# concatenation of string 
	expression = expression + str(num) 

	# update the expression by using set method 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 

		global expression 

		# eval function evaluate the expression 
		# and str function convert the result 
		# into string 
		total = str(eval(expression)) 

		equation.set(total) 

		# initialze the expression variable 
		# by empty string 
		expression = "" 

	# if error is generate then handle 
	# by the except block 
	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("")
    
	equation1.set("")
    
	equation2.set("")


def add(): 
	global a 
	global b
	a = float(expression_field.get())
	b = float(expression_field1.get())
	equation2.set(b-a) 


def read(): 
	global a 
	camera.capture('test.jpg')
	image = open_image('test.jpg')
	a = model.predict(image)
	
	equation1.set(a[0]) 

# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 
    
	# set the background colour of GUI window 
	gui.configure(background="light green") 

	# set the title of GUI window 
	gui.title("Vending Machine") 

	# set the configuration of GUI window 
	gui.geometry("480x250") 

	# StringVar() is the variable class 
	# we create an instance of this class 

	equation2 = StringVar() 

    
	equation = StringVar() 
    
	equation1 = StringVar() 
    

    
	# create the text entry box for 
	# showing the expression .
        
	label = Label(gui, text="Enter the Price",justify=LEFT) 
	label1 = Label(gui, text="Read Money",justify=LEFT) 
	label2 = Label(gui, text="Balance",justify=LEFT) 
    
	expression_field = Entry(gui, textvariable=equation, width=40) 
	expression_field1 = Entry(gui, textvariable=equation1, width=40) 
    
	expression_field2 = Entry(gui, textvariable=equation2, width=40) 
    
    

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
    
	label.grid(row=0,column=0)    

    
	label1.grid(row=1,column=0)  
    
    
	label2.grid(row=2,column=0)  
    
	expression_field.grid(row=0,column=1,columnspan=2)
	expression_field1.grid(row=1,column=1,columnspan=2) 
	expression_field2.grid(row=2,column=1,columnspan=2) 
    
	equation.set('') 
	equation1.set('') 

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button1 = Button(gui, text=' 1 ', fg='black', bg='grey', 
					command=lambda: press(1), height=1, width=12) 
	button1.grid(row=3, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='grey', 
					command=lambda: press(2), height=1, width=12) 
	button2.grid(row=3, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='grey', 
					command=lambda: press(3), height=1, width=12) 
	button3.grid(row=3, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='grey', 
					command=lambda: press(4), height=1, width=12) 
	button4.grid(row=4, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='grey', 
					command=lambda: press(5), height=1, width=12) 
	button5.grid(row=4, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='grey', 
					command=lambda: press(6), height=1, width=12) 
	button6.grid(row=4, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='grey', 
					command=lambda: press(7), height=1, width=12) 
	button7.grid(row=5, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='grey', 
					command=lambda: press(8), height=1, width=12) 
	button8.grid(row=5, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='grey', 
					command=lambda: press(9), height=1, width=12) 
	button9.grid(row=5, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='grey', 
					command=lambda: press(0), height=2, width=12) 
	button0.grid(row=6, column=0) 

	equal = Button(gui, text='Read', fg='black', bg='grey', 
				command=read, height=2, width=12) 
	equal.grid(row=6, column=2) 

	clear = Button(gui, text='Clear', fg='black', bg='grey', 
				command=clear, height=2, width=12) 
	clear.grid(row=6, column='1') 

	Decimal= Button(gui, text='Calulate', fg='black', bg='grey', 
					command=add, height=1, width=45) 
	Decimal.grid(row=7,columnspan=3) 
	# start the GUI 
	gui.mainloop() 
