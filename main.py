import re
import random
import string


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

def check_password(password):
    strong_index = 0
    password_length = len(password)
    with open('password_list.txt', 'r') as txt:
        pass_list = [line.strip().lower() for line in txt.readlines()]

    if password.strip().lower() in pass_list:
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
    return strong_index


def generate_password(length, include_special, include_digits, include_upper):
    characters = string.ascii_lowercase
    if include_special:
        characters += string.punctuation
    if include_digits:
        characters += string.digits
    if include_upper:
        characters += string.ascii_uppercase
    return ''.join(random.choice(characters) for _ in range(length))

