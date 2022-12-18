from PySide6.QtWidgets import QWidget, QHBoxLayout, QSlider
from PySide6.QtCharts import QChart, QLineSeries, QChartView, QSplineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt, QDateTime, QTimer
from PySide6.QtGui import QColor


class TempChart(QWidget):
    def __init__(self, parent):
        super(TempChart, self).__init__(parent)

        self.range = 60
        self.axis_time = QDateTimeAxis()
        self.axis_time.setTitleText("Zeitachse")
        self.axis_time.setTickCount(6)
        self.axis_time.setGridLineColor(QColor("red"))
        self.axis_time.setRange(QDateTime.currentDateTime(), QDateTime.currentDateTime().addSecs(self.range))
        self.currentDate = QDateTime.currentDateTime()
        self.axis_time.setFormat("hh:mm")

        self.axis_percent = QValueAxis()
        self.axis_percent.setTitleText("Prozent")
        self.axis_percent.setRange(0, 100)

        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("x-Achse")
        self.axis_x.setRange(0, 5)

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("y-Achse")
        self.axis_y.setRange(0, 20)

        self.chart = QChart()
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_time, Qt.AlignTop)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.chart.addAxis(self.axis_percent, Qt.AlignRight)

        self.chart_view = QChartView()
        self.chart_view.setChart(self.chart)

        self.slider = QSlider()
        self.slider.valueChanged.connect(self.sliderValueChanged)

        self.my_layout = QHBoxLayout()
        self.my_layout.addWidget(self.chart_view)

        self.my_layout.addWidget(self.slider)


        ### Aufgabe 1
        # Ändern Sie den Zeitbereich der Zeitachse auf 0
        # bis 5 Minuten in der Zukunft. Dafür müssen Sie
        # die alten Werte löschen.

        ### Aufgabe 2
        # Verbinden Sie den QSlider aus Zeile 41 mit dem
        # Werten auf der Prozent und Zeit-Achse. Wird der
        # Slider bewegt, fügt sich ein neuer Wert mit Zeit
        # -Stempel in das Diagramm ein.

        self.setLayout(self.my_layout)

        self.series = QLineSeries()
        self.chart.addSeries(self.series)
        self.series.setName("f(x) = x^2")
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)


        self.series_2 = QLineSeries()
        self.chart.addSeries(self.series_2)
        self.series_2.attachAxis(self.axis_time)
        self.series_2.attachAxis(self.axis_percent)
        self.series_2.setName("Prozent über Zeit")


    def sliderValueChanged(self, value):
        #self.value = value
        #self.drawChart()
        current_time = QDateTime.currentDateTime()
        self.axis_time.setMax(current_time)
        self.series_2.append(current_time.toMSecsSinceEpoch(), value)

    def drawChart(self):
        current_time = QDateTime.currentDateTime()
        self.axis_time.setMax(current_time)
        self.series_2.append(current_time.toMSecsSinceEpoch(), self.value)

