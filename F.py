import sys
import torch
import seaborn as sns
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def generate_data():
    x = torch.linspace(0, 10, 100)
    y = torch.sin(x) + torch.randn_like(x) * 0.2
    return x.numpy(), y.numpy()

# Visualize data using Seaborn
def visualize_data(x, y):
    sns.set(style="whitegrid")
    sns.lineplot(x=x, y=y)
    plt.title("Sample Data Visualization")
    plt.show()


class PlotWindow(QtWidgets.QMainWindow):
    def __init__(self, x, y):
        super().__init__()

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.canvas = MplCanvas(self.central_widget, width=5, height=4, dpi=100)
        self.layout.addWidget(self.canvas)

        self.plot_data(x, y)

    def plot_data(self, x, y):
        self.canvas.axes.plot(x, y)
        self.canvas.axes.set_title('Sample Data Visualization')
        self.canvas.draw()



class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


if __name__ == "__main__":
   
    x, y = generate_data()

    visualize_data(x, y)

    
    app = QtWidgets.QApplication(sys.argv)
    window = PlotWindow(x, y)
    window.show()
    sys.exit(app.exec_())
