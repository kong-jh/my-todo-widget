from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget
)


class TodoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My To-Do Widget")
        self.setFixedSize(300, 400)

        layout = QVBoxLayout()

        # 입력창 + 버튼
        input_layout = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText("Please enter...")
        self.add_button = QPushButton("Add")
        input_layout.addWidget(self.input)
        input_layout.addWidget(self.add_button)

        # 리스트
        self.list_widget = QListWidget()

        # 전체 레이아웃 구성
        layout.addLayout(input_layout)
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

        # 이벤트 연결
        self.add_button.clicked.connect(self.add_todo)

    def add_todo(self):
        text = self.input.text().strip()
        if text:
            self.list_widget.addItem(text)
            self.input.clear()