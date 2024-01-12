# a = 5
# b = 7
# sum = a + b
# print(f"The sum of {a} and {b} = {sum}")

# def add_am(first, second):
#     sum = first + second
#     message = "Sum of " + str(first) + " and " + str(second) + " = " + str(sum)
#     return message

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# print(add_am(num1, num2))

# def calc(a,b,c,d):
#     result = (a + b + c + d)/4
#     return result

# first = int(input("Enter first number : "))
# second = int(input("Enter second number : "))
# third = int(input("Enter third number : "))
# fourth = int(input("Enter fourth number : "))
# my_mean = calc(first,second,third,fourth)
# print(f"Mean is {my_mean}")

# PI = 3.142

# def area_of_circle(r):
#     area = (r * r) * PI
#     return area

# print(area_of_circle(3))


# def add_am(first, second):
#     sum = first + second
#     return sum

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# result = add_am(num1, num2) * 2
# print(f"Multiple is {result}")

# a = 3.5
# print(type(a))

# fruits = ["apple", "banana", "cherry",True]
# x,y,z,a = fruits
# print(a)

# print(10//3)

# import random

# print(random.randrange(1, 10, 3)) 
# for x in range(1,10):
#     if x % 2 == 0:
#         print(f"{x} is EVEN")
#     else:
#         print(x)


# txt = "The best things in life are free!"
# word = input("Enter Word to Swap : ")
# if word in txt:
# 	word = "E DEY"
# changed_txt = f"The best things in life are {word}"
# print(changed_txt)

# PI = 3.142

# def area_of_circle(r = 3):
#     area = PI * (r*r)
#     return area

# print(area_of_circle())
# print(area_of_circle(6))

# a = "ELIJAH"
# b = a.lower()
# print(b)

# txt = "The best things in life are free!"
# new_txt = txt.replace("free", "E DEY")
# print(new_txt)

import tkinter as tk
from tkinter import ttk
import platform

# function to split email
def email_splitter(mail):
    username = mail.split('@')[0]
    host = mail.split('@')[1]
    #host = mail.split('@')[1].split(".")[1][1].upper()
    response = f"Your username is {username}\nYour Hosting Company is {host}"
    return response

# mail = email_splitter("martins@gmail.com")
# print(mail)

# Function to get details from Operating System
def get_os_details():
    system_info = f"System: {platform.system()} {platform.version()}\n"
    machine_info = f"Machine: {platform.machine()}\n"
    processor_info = f"Processor: {platform.processor()}\n"
    architecture = f"Architecture: {platform.architecture()}\n"
    node = f"Node: {platform.node()}\n"
    details = f"{system_info}, {machine_info}, {processor_info}, {architecture}, {node}"
    return details


# Function to show Operating System details
def show_os_details():
    os_details = get_os_details()
    os_result_text.set(os_details)

# Function to show splitted Email
def on_submit():
    email = entry.get()
    result_text.set(email_splitter(email))
    entry.delete(0, tk.END)

# GUI starts from here
# Create the main window GUI in tkinter
app = tk.Tk()
app.title("Email Splitter")
app.geometry("400x400")

# Create a frame to organize the input field and buttons
frame = tk.Frame(app)
frame.pack(pady=10)

# Create input label and entry
label = tk.Label(frame, text="Enter your email:")
label.grid(row=0, column=0, pady=10)
entry = tk.Entry(frame)
entry.grid(row=0, column=1, pady=10)

# Create submit button
submit_button = tk.Button(frame, text="Split", command=on_submit)
submit_button.grid(row=1, column=0, padx=5, pady=10)

# Create exit button
exit_button = tk.Button(frame, text='Exit', command=app.destroy)
exit_button.grid(row=1, column=1, padx=5, pady=10)

# Create a label to display the result
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, font=("Arial", 14), fg="green")
result_label.pack(pady=10)

# Create a horizontal rule
separator = ttk.Separator(app, orient='horizontal')
separator.pack(fill='x', pady=10)

# Create a button to fetch and display OS details
details_button = tk.Button(frame, text="Show OS Details", command=show_os_details)
details_button.grid(row=2, column=0, columnspan=5, padx=5, pady=10)

# Create a label to display the OS details with adjusted font and color
os_result_text = tk.StringVar()
os_result_label = tk.Label(app, textvariable=os_result_text, font=("Arial", 10), fg="blue")
os_result_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
