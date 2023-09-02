from PySide6.QtWidgets import QComboBox

class combo_box(QComboBox):
    def __init__(self,items):
        super().__init__()
        self.addItems(items)
        self.textValue = items[0]
        self.set_button()

    def set_button(self):
        self.currentTextChanged.connect(self.operation)

    def operation(self,text):
        self.textValue = text
        