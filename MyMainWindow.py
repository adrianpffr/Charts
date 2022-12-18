from PySide6.QtWidgets import QMainWindow
from RoboChart import RoboChart

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("QChartView")

        self.setCentralWidget(RoboChart(self))
