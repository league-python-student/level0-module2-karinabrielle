import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3 (including 0 and 3)


    messagebox.showinfo(message="This is the magic 8 ball...")
    messagebox.showinfo(message="It will answer any yes or no question you ask")
    simpledialog.askstring(title="",prompt="Now type in your yes or no question")



    num = random.randint(0, 3)

    if num ==0:
        messagebox.showinfo(message="yes")
    if num ==1:
        messagebox.showinfo(message="no")
    if num ==2:
        messagebox.showinfo(message="maybe you should ask google")
    if num ==3:
        messagebox.showinfo(message="...")
        messagebox.showinfo(message="ERROR")
        messagebox.showinfo(message="WARNING... SOMETHING BAD WILL HAPPEN")
        messagebox.showinfo(message="do not worry.......error.....*disappears")
# If num = 0


        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
