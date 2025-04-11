import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from playsound import playsound
import threading

def resource_path(relative_path):
    """ Get absolute path to resource, works for .exe and .py """
    try:
        base_path = sys._MEIPASS  # Used by PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class RickPopup(QLabel):
    def __init__(self):
        super().__init__()

        # Load and set the transparent PNG
        pixmap = QPixmap(resource_path("rick.png"))
        self.setPixmap(pixmap)

        # Set window properties (frameless, always on top, transparent background)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(pixmap.size())

        # Center the window
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

        # Play audio in a separate thread to avoid blocking UI
        threading.Thread(target=self.play_audio_and_close, daemon=True).start()

    def play_audio_and_close(self):
        playsound(resource_path("rickr.mp3"))
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rick = RickPopup()
    rick.show()
    sys.exit(app.exec_())
