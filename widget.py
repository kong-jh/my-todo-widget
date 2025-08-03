import json
import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget
)

DATA_FILE = "todos.json"

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
        self.todo_list = QListWidget()

        # 전체 레이아웃 구성
        layout.addLayout(input_layout)
        layout.addWidget(self.todo_list)
        self.setLayout(layout)

        # 이벤트 연결
        self.add_button.clicked.connect(self.add_todo)
        self.input.returnPressed.connect(self.add_todo)

        # 저장된 목록 불러오기
        self.load_todos()

    def add_todo(self):
        text = self.input.text().strip()
        if text:
            self.todo_list.addItem(text)
            self.input.clear()
            self.save_todos()

    def load_todos(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    todos = json.load(f)
                    for todo in todos:
                        self.todo_list.addItem(todo)
            except Exception as e:
                print(f"불러오기 실패: {e}")

    def save_todos(self):
        todos = []
        for i in range(self.todo_list.count()):
            todos.append(self.todo_list.item(i).text())
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(todos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"저장 실패: {e}")

    def closeEvent(self, event):
        self.save_todos()
        event.accept()