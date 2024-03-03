import random
import sys
from tkinter import messagebox, Tk, simpledialog


# from playsound import playsound

wekncrzpasfdkjhcfjse = random.randint(0, 999)

messagebox.showinfo(message="Welcome to the Crack Open The Safe Simulator!")
messagebox.showinfo(message="Obviously, your objective is to try to crack open a safe, and your answer has to have a total of 6 digits.")
messagebox.showinfo(message="Good luck!!!")
def crack_the_safe():
    for answer in range(999999999999999999999999):
        answer = simpledialog.askstring(title="safe", prompt="Type in a code to open a safe")
        answer2 = int(answer)
        if answer2 < 100000 :
            messagebox.showinfo(message="Your answer has to have a total of 6 digits...")
        if answer2 > 999999 :
            messagebox.showinfo(message="Your answer has to only have 6 digits...")
        if answer2 == 999999:
            messagebox.showinfo(message="CONGRATULATIONS!!! You have cracked open the safe! Click okay to exit the program.")
            messagebox.showinfo(message="leaving the program now...")
            sys.exit(0)
    # TODO: Your mission: Use the try_code method to crack the safe
    #  by trying all possible combinations

    # guess = simpledialog.askstring(title="safe", prompt="Type in a code to open a safe")

    # ======================= DO NOT EDIT THE CODE BELOW =========================



def try_code(guess):
    print("trying " + str(guess))

    secret_code = 999999 - wekncrzpasfdkjhcfjse

    if guess == secret_code:
        messagebox.showinfo(None, "Congratulations! You cracked the safe with " + str(guess))
        #  play_the_sound_of_success()
        sys.exit(0)


# def play_the_sound_of_success():
    #  playsound('me-gusta.wav')
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    crack_the_safe()
