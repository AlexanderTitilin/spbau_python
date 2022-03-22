import sys
import requests
from PySide6 import QtWidgets, QtCore


class Reader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.thread = None
        self.text = QtWidgets.QLabel()
        self.text.setMaximumWidth(800)
        self.text.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.url = QtWidgets.QLineEdit("Введите ссылку")
        self.buttonGet = QtWidgets.QPushButton("Получить посты")
        self.buttonGet.clicked.connect(self.makeThread)
        self.buttonPrev = QtWidgets.QPushButton("<")
        self.buttonPrev.clicked.connect(self.showPreviousPost)
        self.buttonNext = QtWidgets.QPushButton(">")
        self.buttonNext.clicked.connect(self.showNextPost)
        self.baseLayout = QtWidgets.QVBoxLayout(self)
        buttonLayout = QtWidgets.QHBoxLayout()
        self.baseLayout.addWidget(self.text)
        self.baseLayout.addWidget(self.url)
        buttonLayout.addWidget(self.buttonPrev)
        buttonLayout.addWidget(self.buttonGet)
        buttonLayout.addWidget(self.buttonNext)
        self.baseLayout.addLayout(buttonLayout)

    @QtCore.Slot()
    def makeThread(self):
        self.thread = DvachThread(self.url.text())
        self.text.setText(self.thread.posts[self.thread.currentPostIndex])

    @QtCore.Slot()
    def showNextPost(self):
        self.thread.nextPost()
        self.text.setText(self.thread.posts[self.thread.currentPostIndex])

    @QtCore.Slot()
    def showPreviousPost(self):
        self.thread.previousPost()
        self.text.setText(self.thread.posts[self.thread.currentPostIndex])


class DvachThread:
    def __init__(self, url: str) -> None:
        self.posts = self.getPosts(self.makeJson(url))
        self.currentPostIndex = 0

    def nextPost(self) -> None:
        self.currentPostIndex = (self.currentPostIndex + 1) % len(self.posts)

    def previousPost(self) -> None:
        self.currentPostIndex = (self.currentPostIndex - 1) % len(self.posts)

    def getCurrentPost(self) -> str:
        return self.posts[self.currentPostIndex]

    def getPosts(self, url: str) -> list:
        response = requests.get(url)
        posts = [i["comment"] for i in response.json()["threads"][0]["posts"]]
        return posts

    def makeJson(self, url: str) -> str:
        return url.strip().replace("html", "json")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Reader()
    widget.resize(800, 400)
    widget.show()
    sys.exit(app.exec())
