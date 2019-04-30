#Klasy i dziedziczenie

class Widget:
    def __init__(self, label):
        self.label = label

class Button(Widget):
    def __init__(self, label, size):
        super().__init__(label)
        self.size = size

    def handle_click(self):
        return "Klik!"

a = Widget('my widget')
b = Button('my button', 'large')
print(a.label)
print(b.label, b.size)
print(b.handle_click())