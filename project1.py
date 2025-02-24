import random

def gamewin(comp, you):
    if comp == you:
        return None
    if comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 'r':
        if you == 'p':
            return False
        elif you == 's':
            return True
print("Comp turn turn : rock(r), paper(p), scissor(s) ")
randno = random.randint(1,3)
print(randno)
if randno == 1:
    comp = 'r'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 's'

you = input("your turn : rock(r), paper(p), scissor(s) ")
a = gamewin(comp, you)
print (f"computer choose {comp}")
print (f"you choose {you}")

if a == None :
    print("the game is a tie!")
elif a :
    print("you win!")
else :
    print("you lose!")
# import random
# import tkinter as tk
# from tkinter import messagebox

# def gamewin(comp, you):
#     if comp == you:
#         return None
#     win_cases = [('r', 's'), ('s', 'p'), ('p', 'r')]
#     return (you, comp) in win_cases

# def play_game(choice):
#     comp = random.choice(['r', 'p', 's'])
#     result = gamewin(comp, choice)

#     choices = {'r': "Rock", 'p': "Paper", 's': "Scissors"}
    
#     computer_choice_label.config(text=f"Computer chose: {choices[comp]}")
#     user_choice_label.config(text=f"You chose: {choices[choice]}")
    
#     if result is None:
#         result_label.config(text="It's a Tie!", fg="blue")
#     elif result:
#         result_label.config(text="You Win! 🎉", fg="green")
#     else:
#         result_label.config(text="You Lose! 😢", fg="red")

# # Create main window
# root = tk.Tk()
# root.title("Rock Paper Scissors")
# root.geometry("400x400")
# root.config(bg="#f4f4f4")

# # Title Label
# title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="#f4f4f4")
# title_label.pack(pady=10)

# # Display choices
# computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12), bg="#f4f4f4")
# computer_choice_label.pack(pady=5)

# user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 12), bg="#f4f4f4")
# user_choice_label.pack(pady=5)

# # Result Label
# result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f4f4f4")
# result_label.pack(pady=10)

# # Buttons
# button_frame = tk.Frame(root, bg="#f4f4f4")
# button_frame.pack(pady=20)

# rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play_game('r'))
# rock_button.grid(row=0, column=0, padx=5)

# paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play_game('p'))
# paper_button.grid(row=0, column=1, padx=5)

# scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play_game('s'))
# scissors_button.grid(row=0, column=2, padx=5)

# # Run the application
# root.mainloop()
