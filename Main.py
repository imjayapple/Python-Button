# Import the tkinter library as "tk"
import tkinter as tk

# Basic function
def button1_clicked():
    print("Yes")

def button2_clicke():
    print("No")
# Create the main application window
root = tk.Tk()

# Creating a button with specified options
button1 = tk.Button(root, 
                   text="Yes", 
                   command=button1_clicked)


button2 = tk.Button(root,
                     text = "No",
                     command=button2_clicke)


button1.pack(padx=20, pady=20)
button2.pack(padx=20, pady=20)

root.mainloop()