import tkinter as tk
from tkinter import messagebox
import csv

#voting function
def vote(candidate, voter_id):
    
#validate the voter
    if not validate_identifier(voter_id):
        return
    
#check for duplicate voter
    if check_duplicate(voter_id):
        messagebox.showerror("Duplicate Identifier", "This identifier has already been used.")
        return
    
#record the vote
    with open('votes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([voter_id, candidate])

    messagebox.showinfo("Vote Recorded", f"Voted for {candidate} as best artist")

    error_label.config(text="")

# voter id function 
def validate_identifier(voter_id):

#make sure the identifier is a positive numeric value
    if not voter_id.isdigit():
        if any(char in voter_id for char in ['.', ',']):
            error_label.config(text="Floating points are not allowed.", fg="red")
        elif '-' in voter_id:
            error_label.config(text="Only positive numbers are allowed.", fg="red")
        else:
            error_label.config(text="Only numeric values are allowed.", fg="red")
        return False
    if int(voter_id) <= 0:
        error_label.config(text="Only positive numbers are allowed.", fg="red")
        return False
    error_label.config(text="")
    return True

#function for duplicate ids
def check_duplicate(voter_id):
    try:
        with open('votes.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == voter_id:
                    return True
    except FileNotFoundError:
        return False
    return False

#voting button function
def on_vote():
    voter_id = entry_id.get().strip()
    if var.get() == 'Eminem':
        vote('Eminem', voter_id)
    elif var.get() == 'Taylor Swift':
        vote('Taylor Swift', voter_id)
    elif var.get() == 'Morgan Wallen':
        vote('Morgan Wallen', voter_id)
    else:
        #error if no one is chose
        error_label.config(text="Select a candidate", fg="red")

#gui function
def create_gui():
    global entry_id, var, error_label

    root = tk.Tk()
    root.title("Voting Application")
    root.geometry("300x300")
    root.resizable(False, False)

    tk.Label(root, text="Unique Identifier:").pack(pady=10)
    
    entry_id = tk.Entry(root)
    entry_id.pack(pady=5)

    tk.Label(root, text="Select candidate for best artist:").pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=10)

#radio buttons for candidates
    var = tk.StringVar(value="None")
    tk.Radiobutton(frame, text="Eminem", variable=var, value="Eminem").pack(anchor=tk.CENTER)
    tk.Radiobutton(frame, text="Taylor Swift", variable=var, value="Taylor Swift").pack(anchor=tk.CENTER)
    tk.Radiobutton(frame, text="Morgan Wallen", variable=var, value="Morgan Wallen").pack(anchor=tk.CENTER)

#submit button
    tk.Button(root, text="Vote", command=on_vote).pack(pady=20)

    error_label = tk.Label(root, text="", fg="red")
    error_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
