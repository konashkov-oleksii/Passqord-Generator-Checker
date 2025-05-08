import re
import random
import string
import tkinter as tk
from tkinter import ttk

color_text = '#9e9f9d'
color_background_app = '#0b0c0e'
color_background_frame = '#0d0e12'
color_background_ui = '#111316'
color_button_bg = '#2b2b2b'
color_button_active = '#404040'
color_entry_bg = '#2e2e2e'
color_entry_fg = 'white'
color_result_strong = 'green'
color_result_medium = 'orange'
color_result_weak = 'red'

button_style = {
    'bg': color_button_bg,
    'fg': 'white',
    'activebackground': color_button_active,
    'activeforeground': 'white',
    'bd': 1,
    'relief': 'flat',
    'font': ('Arial', 11)
}

entry_style = {
    'bg': color_entry_bg,
    'fg': color_entry_fg,
    'insertbackground': color_entry_fg,
    'bd': 0,
    'font': ('Arial', 12)
}

def check_password():
    strong_index = 0
    password = pass_input.get()
    password_length = len(password)
    with open('password_list.txt', 'r') as txt:
        pass_list = [line.strip().lower() for line in txt.readlines()]

    if password.strip().lower() in pass_list:
        result_label.config(text="Password is weak.", fg=color_result_weak)
        return

    if password_length >= 12:
        strong_index += 2
    elif password_length >= 8:
        strong_index += 1

    if re.search(r'[a-z]', password):
        strong_index += 1
    if re.search(r'[A-Z]', password):
        strong_index += 1
    if re.search(r'\d', password):
        strong_index += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strong_index += 1
    if re.search(r'(..+)\1', password):
        strong_index -= 1

    if strong_index >= 5:
        result_label.config(text="Password is strong!", fg=color_result_strong)
    elif strong_index >= 3:
        result_label.config(text="Password is medium.", fg=color_result_medium)
    else:
        result_label.config(text="Password is weak.", fg=color_result_weak)

def generate_password(length, include_special, include_digits, include_upper):
    characters = string.ascii_lowercase
    if include_special:
        characters += string.punctuation
    if include_digits:
        characters += string.digits
    if include_upper:
        characters += string.ascii_uppercase
    return ''.join(random.choice(characters) for _ in range(length))

def gen_pass():
    password = generate_password(random.randint(12, 21), checkboxes['spec_symbol'].get(), checkboxes['digits'].get(), checkboxes['up_case'].get())
    pass_generated.config(state="normal")
    pass_generated.delete(0, tk.END)
    pass_generated.insert(0, password)
    pass_generated.config(state="readonly")

root = tk.Tk()
root.title("Password Generator")
root.geometry('600x300')
root.configure(bg=color_background_app)

frame_check = tk.Frame(root, bg=color_background_frame)
frame_check.place(relheight=1, relwidth=0.35, relx=0.15)

tk.Label(frame_check, text="Check Password", fg='white', bg=color_background_frame, font=('Arial', 14, 'bold')).pack(pady=(20, 10))

pass_input = tk.Entry(frame_check, **entry_style)
pass_input.pack(pady=5, padx=10, fill='x')

btn_check = tk.Button(frame_check, text='Check your pass', command=check_password, **button_style)
btn_check.pack(pady=10)

result_label = tk.Label(frame_check, text="", font=("Arial", 12), bg=color_background_ui, fg=color_text)
result_label.pack(pady=10)

frame_generate = tk.Frame(root, bg=color_background_frame)
frame_generate.place(relheight=1, relwidth=0.35, relx=0.55)

tk.Label(frame_generate, text="Generate Password", fg='white', bg=color_background_frame, font=('Arial', 14, 'bold')).pack(pady=(20, 10))

checkboxes = {
    'spec_symbol': tk.IntVar(),
    'digits': tk.IntVar(),
    'up_case': tk.IntVar()
}

tk.Checkbutton(frame_generate, text="Include special characters", variable=checkboxes['spec_symbol'], bg=color_background_ui, fg=color_text, selectcolor=color_background_frame).pack(anchor='w', padx=10)
tk.Checkbutton(frame_generate, text="Include digits", variable=checkboxes['digits'], bg=color_background_ui, fg=color_text, selectcolor=color_background_frame).pack(anchor='w', padx=10)
tk.Checkbutton(frame_generate, text="Include upper case", variable=checkboxes['up_case'], bg=color_background_ui, fg=color_text, selectcolor=color_background_frame).pack(anchor='w', padx=10)

btn_generate = tk.Button(frame_generate, text='Generate pass', command=gen_pass, **button_style)
btn_generate.pack(pady=10)

pass_generated = tk.Entry(frame_generate, state="readonly", **entry_style)
pass_generated.pack(pady=5, padx=10, fill='x')

root.mainloop()
