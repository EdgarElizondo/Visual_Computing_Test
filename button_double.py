from PySide6.QtWidgets import QPushButton

class button_double_text(QPushButton):
    def __init__(self, text1, text2,function = None,*args):
        super().__init__()
        self.text1 = text1
        self.text2 = text2
        self.function = function
        self.value = True
        self.elem = args
        self.set_button()

    def set_button(self):
        self.setText(self.text1)
        self.clicked.connect(self.operation)

    def operation(self):

        if self.value:
            self.setText(self.text2)
            self.value = False
        else:
            self.setText(self.text1)
            self.value = True

        if self.function == "modified_layout":
            self.modified_layout(self.elem[0], self.elem[1])

    def modified_layout(self,layout,label):
        if self.value:
            layout.addWidget(label)
        else:
            layout.removeWidget(label)