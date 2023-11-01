from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox

import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        # Define Widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (Hours):")
        self.time_line_edit = QLineEdit()

        self.metric_dropdown = QComboBox()
        self.metric_dropdown.addItems(["Metric (km)", "Imperial (miles)"])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)

        self.output_label = QLabel("")

        # Add Widgets to Grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(self.metric_dropdown, 0, 2)
        grid.addWidget(calculate_button, 2, 0, 1, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        # Get distance and time from the input boxes
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())

        # Calculate average speed
        speed = distance/time

        # check what user chose in the combo
        if self.metric_dropdown.currentText() == "Metric (km)":
            speed = round(speed, 2)
            unit = "km/h"
        if self.metric_dropdown.currentText() == "Imperial (miles)":
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        # Display the Result
        self.output_label.setText(f"Average speed: {speed} {unit}")


app = QApplication(sys.argv)
age_calculator = SpeedCalculator()
age_calculator.show()
sys.exit(app.exec())