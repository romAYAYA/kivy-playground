from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random


class RandomIntGeneratorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.label = Label(text="Enter the range for random integers:")
        self.layout.add_widget(self.label)

        self.min_input = TextInput(hint_text="Min", input_type='number', multiline=False)
        self.layout.add_widget(self.min_input)

        self.max_input = TextInput(hint_text="Max", input_type='number', multiline=False)
        self.layout.add_widget(self.max_input)

        self.generate_button = Button(text="Generate Random Integers", on_press=self.generate_random_integers)
        self.layout.add_widget(self.generate_button)

        self.result_label = Label(text="", halign='center')
        self.layout.add_widget(self.result_label)

        return self.layout

    def generate_random_integers(self, instance):
        try:
            min_value = int(self.min_input.text)
            max_value = int(self.max_input.text)
            if min_value >= max_value:
                raise ValueError("Minimum value must be smaller than maximum value.")
            random_int = random.randint(min_value, max_value)
            self.result_label.text = f"Random Integer: {random_int}"
        except ValueError as e:
            self.result_label.text = str(e)


if __name__ == "__main__":
    RandomIntGeneratorApp().run()
