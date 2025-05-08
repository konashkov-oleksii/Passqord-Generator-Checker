from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
import re
import random
import string

class PasswordApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal', padding=20, spacing=20, background_color=(0.05, 0.05, 0.05, 1))

        check_layout = BoxLayout(orientation='vertical', spacing=10)
        check_label = Label(text='[b]Check Password[/b]', markup=True, font_size='18sp', color=(1, 1, 1, 1))
        self.pass_input = TextInput(hint_text='Enter password', background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1))

        btn_check = Button(text='Check your pass', size_hint_y=None, height=40, background_color=(0.3, 0.3, 0.3, 1))
        btn_check.bind(on_press=self.check_password)

        self.result_label = Label(font_size='14sp', color=(0.7, 0.7, 0.7, 1))

        check_layout.add_widget(check_label)
        check_layout.add_widget(self.pass_input)
        check_layout.add_widget(btn_check)
        check_layout.add_widget(self.result_label)

        gen_layout = BoxLayout(orientation='vertical', spacing=10)
        gen_label = Label(text='[b]Generate Password[/b]', markup=True, font_size='18sp', color=(1, 1, 1, 1))

        self.spec_checkbox = CheckBox()
        self.digits_checkbox = CheckBox()
        self.upper_checkbox = CheckBox()

        checkbox_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        checkbox_layout.add_widget(Label(text='Include special characters'))
        checkbox_layout.add_widget(self.spec_checkbox)
        checkbox_layout.add_widget(Label(text='Include digits'))
        checkbox_layout.add_widget(self.digits_checkbox)
        checkbox_layout.add_widget(Label(text='Include upper case'))
        checkbox_layout.add_widget(self.upper_checkbox)

        btn_generate = Button(text='Generate pass', size_hint_y=None, height=40, background_color=(0.3, 0.3, 0.3, 1))
        btn_generate.bind(on_press=self.gen_pass)

        self.pass_generated = TextInput(readonly=True, background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1))

        gen_layout.add_widget(gen_label)
        gen_layout.add_widget(checkbox_layout)
        gen_layout.add_widget(btn_generate)
        gen_layout.add_widget(self.pass_generated)

        layout.add_widget(check_layout)
        layout.add_widget(gen_layout)

        return layout

    def check_password(self, instance):
        password = self.pass_input.text
        strong_index = sum([bool(re.search(pattern, password)) for pattern in [r'[a-z]', r'[A-Z]', r'\d', r'[!@#$%^&*(),.?":{}|<>]']])

        if len(password) >= 12: strong_index += 1

        self.result_label.text = ['Weak', 'Medium', 'Strong'][min(strong_index, 2)]

    def gen_pass(self, instance):
        length = random.randint(12, 21)
        characters = string.ascii_lowercase

        if self.spec_checkbox.active: characters += string.punctuation
        if self.digits_checkbox.active: characters += string.digits
        if self.upper_checkbox.active: characters += string.ascii_uppercase

        self.pass_generated.text = ''.join(random.choice(characters) for _ in range(length))

if __name__ == '__main__':
    PasswordApp().run()
