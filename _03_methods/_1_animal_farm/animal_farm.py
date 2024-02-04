import tkinter as tk
from tkinter import simpledialog, Tk, messagebox
from PIL import Image, ImageTk
# from playsound import playsound

window = None


def animals():
    global window
    window = Tk()
    window.withdraw()

    # TODO 1. Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.

    # TODO 2. Make it so that the user can keep entering new animals.

    # TODO 3. If the user enters 'exit', stop the program

    messagebox.showinfo(message="We have an animal farm and you will be able to see some animals! :)")
    messagebox.showinfo(message="Type in a the animal you want to see, and the options are a cat, dog, cow, duck, llama, and a scary guard dog :P.")
    messagebox.showinfo(message="For example, if I want to see a cat, I just type in the word cat")
    animal = simpledialog.askstring(title="THE FARM", prompt="Type in your animal you want to see. If you want to leave the animal farm, just type in the word exit.")

    if animal == "cat":
        show_image("cat.jpg")
    if animal == "dog":
        show_image("dog.jpg")
    if animal == "cow":
        show_image("cow.jpg")
    if animal == "duck":
        show_image("duck.jpg")
    if animal == "llama":
        show_image("llama.jpg")


# ======================= DO NOT EDIT THE CODE BELOW =========================

def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    # Put the image on the Tk window used by simpledialog so that when the
    # window with the image is closed, the interpreter moves to the next
    # line of code
    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    # Blocks so picture can be shown--resumes when picture window is closed
    window.mainloop()

    # Regenerate a new window after closing so more simpledialogs and
    # images can be shown
    window = Tk()
    window.withdraw()


def moo():
    show_image('cow.jpg')
    playsound('moo.wav')


def quack():
    show_image('duck.jpg')
    playsound('quack.wav')


def woof():
    show_image('dog.jpg')
    playsound('woof.wav')


def meow():
    show_image('cat.jpg')
    playsound('meow.wav')


def llama_scream():
    show_image('llama.jpg')
    playsound('llama.wav')


if __name__ == '__main__':
    animals()
