from PySide6.QtWidgets import QWidget, QHBoxLayout, QSlider, QDial, QPushButton
from PySide6.QtCharts import QChart, QLineSeries, QChartView, QSplineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt, QDateTime, QTimer
from PySide6.QtGui import QColor


class RoboChart(QWidget):
    def __init__(self, parent):
        super(RoboChart, self).__init__(parent)

        self.axis_percent = QValueAxis()

        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("x-Achse")
        self.axis_x.setRange(-5, 105)
        self.axis_x.hide()

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("y-Achse")
        self.axis_y.setRange(-5, 105)
        self.axis_y.hide()

        self.dial1 = QDial()
        self.dial1.valueChanged.connect(self.dial1Changed)

        self.dial2 = QDial()
        self.dial2.setWrapping(False)
        self.dial2.valueChanged.connect(self.dial2Changed)

        self.deleteButton = QPushButton()
        self.deleteButton.setText("Delete")
        self.deleteButton.clicked.connect(self.clearChart)


        self.chart = QChart()
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.chart.addAxis(self.axis_percent, Qt.AlignRight)

        self.chart_view = QChartView()
        self.chart_view.setChart(self.chart)

        self.my_layout = QHBoxLayout()
        self.my_layout.addWidget(self.chart_view)
        self.my_layout.addWidget(self.dial1)
        self.my_layout.addWidget(self.dial2)
        self.my_layout.addWidget(self.deleteButton)


        self.setLayout(self.my_layout)

        self.series = QLineSeries()
        self.chart.addSeries(self.series)
        self.series.setName("Robo")
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

    def dial1Changed(self, value):
        self.series.append(self.dial2.value(), value)

    def dial2Changed(self, value):
        self.series.append(value, self.dial1.value())

    def clearChart(self):
        self.series.clear()



