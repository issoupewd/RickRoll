import sys
import os
import threading
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from playsound import playsound

def resource_path(relative_path):
    """ Get absolute path to resource, works for .exe and .py """
    try:
        base_path = sys._MEIPASS  # Used by PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Define a signal emitter object to communicate from the thread
class Emitter(QObject):
    done = pyqtSignal()

class RickPopup(QLabel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.emitter = Emitter()
        self.emitter.done.connect(self.close_and_exit)

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

        # Start playing sound
        threading.Thread(target=self.play_audio_and_emit, daemon=True).start()

    def play_audio_and_emit(self):
        playsound(resource_path("rickr.mp3"))
        self.emitter.done.emit()

    def close_and_exit(self):
        self.close()
        self.app.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rick = RickPopup(app)
    rick.show()
    sys.exit(app.exec_())
