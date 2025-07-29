import sys
from PyQt5.QtWidgets import QApplication
from widget import TodoWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoWidget()
    window.show()
    sys.exit(app.exec_())