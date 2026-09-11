class ZoneVisualisation2D(QWidget):
    def __init__(self, simulation, parent=None):
        super().__init__(parent)
        self.simulation = simulation

        self.setMinimumSize(600, 600)

        self.setStyleSheet("background-color: #0B1E28;")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        centre_x = self.width() / 2
        centre_y = self.height() / 2
