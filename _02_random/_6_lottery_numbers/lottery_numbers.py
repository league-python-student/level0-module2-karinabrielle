import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket

    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket



    num = random.randint(1, 60)
    num2 = random.randint(1, 60)
    num3 = random.randint(1, 60)
    num4 = random.randint(1, 60)
    num5 = random.randint(1, 60)
    num6 = random.randint(1, 60)
    winner = random.randint(1, 60)
    winner2 = random.randint(1, 60)
    winner3 = random.randint(1, 60)
    winner4 = random.randint(1, 60)
    winner5 = random.randint(1, 60)
    winner6 = random.randint(1, 60)

    messagebox.showinfo(message="You will get a lottery ticket with some numbers on it. Here is your lottery ticket, and good luck!")
    messagebox.showinfo(title="lottery ticket",message="your ticket : " + (str(num))+", "+(str(num2))+", "+(str(num3))+", "+(str(num4))+", "+(str(num5))+", "+(str(num6)) + "\n winner : " + (str(winner))+", "+(str(winner2))+", "+(str(winner3))+", "+(str(winner4))+", "+(str(winner5))+", "+(str(winner6)))







