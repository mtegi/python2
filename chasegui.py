from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QSizePolicy, QMessageBox

from chase import Chase


def show_popout(msg, title):
    dialog = QMessageBox()
    dialog.setWindowTitle(title)
    dialog.setText(msg)
    dialog.setIcon(QMessageBox.Information)
    dialog.exec_()


def show_no_sheep_warning():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("Add some sheep !")
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()


class ChaseGui(QtWidgets.QMainWindow):
    def __init__(self, chaseObject):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.step = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SheepLabel = QtWidgets.QLabel(self.centralwidget)
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.chase = chaseObject
        pen_width = self.chase.init_pos_limit / 22
        self.sheepPen = QtGui.QPen()
        self.sheepPen.setWidth(pen_width)
        self.sheepPen.setColor(Qt.blue)
        self.wolfPen = QtGui.QPen()
        self.wolfPen.setWidth(pen_width)
        self.wolfPen.setColor(Qt.red)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 568, 800, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.step.setObjectName("step")
        self.step.setText("Step")
        self.step.clicked.connect(self.on_step_clicked)
        self.horizontalLayout.addWidget(self.step)
        self.reset.setObjectName("reset")
        self.reset.setText("Reset")
        self.reset.clicked.connect(self.on_reset_clicked)
        self.horizontalLayout.addWidget(self.reset)
        self.SheepLabel.setGeometry(QtCore.QRect(0, 0, 800, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SheepLabel.setFont(font)
        self.SheepLabel.setObjectName("SheepLabel")
        self.canvas.setObjectName("canvas")
        self.canvas.setGeometry(QtCore.QRect(0, self.SheepLabel.height(), 800, 555))
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.setAlignment(Qt.AlignCenter)
        self.canvas.setStyleSheet("QLabel {background-color: darkGreen;}")
        pixmap = QtGui.QPixmap(1.5 * self.chase.init_pos_limit, 1.5 * self.chase.init_pos_limit)
        pixmap.fill(Qt.white)
        self.canvas.setPixmap(pixmap)
        self.canvas.mousePressEvent = self.on_mouse_click
        self.setCentralWidget(self.centralwidget)
        self.updateSheepLabel()
        self.render()

    def updateSheepLabel(self):
        self.SheepLabel.setText("Alive Sheep:" + self.chase.alive_sheep.__str__())

    def draw_something(self):
        painter = QtGui.QPainter(self.canvas.pixmap())
        painter.setPen(self.sheepPen)
        painter.drawPoint(0, 0)
        painter.end()
        self.update()

    def draw_wolf(self, painter):
        wolf_pos = QPoint()
        wolf_pos.setX(self.chase.wolf.x)
        wolf_pos.setY(self.chase.wolf.y)
        painter.setPen(self.wolfPen)
        painter.drawPoint(self.convert_animal_to_pixmap(wolf_pos))

    def draw_sheep(self, painter):
        painter.setPen(self.sheepPen)
        for s in self.chase.sheep_arr:
            if s is not None:
                sheep_pos = QPoint()
                sheep_pos.setX(s.x)
                sheep_pos.setY(s.y)
                painter.drawPoint(self.convert_animal_to_pixmap(sheep_pos))

    def on_step_clicked(self):
        if len(self.chase.sheep_arr) == 0 or self.chase.sheep_arr == [None] * len(self.chase.sheep_arr):
            show_no_sheep_warning()
        else:
            self.chase.step()
            if self.chase.wolf.eaten_sheep_index is not None:
                show_popout("Sheep no." + str(self.chase.wolf.eaten_sheep_index + 1) + " was eaten.", "A sheep was "
                                                                                                      "eaten !")
            self.render()

    def convert_to_animal_pos(self, pos):
        point = QPoint()
        point.setX(pos.x() - self.width() / 2)
        point.setY(pos.y() - self.height() / 2 + self.horizontalLayoutWidget.height() - self.SheepLabel.height())
        return point

    def convert_animal_to_pixmap(self, pos):
        point = QPoint()
        point.setX(pos.x() + self.canvas.pixmap().size().height() / 2)
        point.setY(pos.y() + self.canvas.pixmap().size().height() / 2)
        return point

    def on_mouse_click(self, e):
        animal_pos = self.convert_to_animal_pos(e.pos())
        if e.button() == Qt.LeftButton:
            self.chase.add_sheep(animal_pos.x(), animal_pos.y())
            self.updateSheepLabel()
        elif e.button() == Qt.RightButton:
            self.chase.wolf.setPos(animal_pos.x(), animal_pos.y())
        self.render()

    def on_reset_clicked(self):
        self.chase.reset()
        self.render()

    def render(self):
        painter = QtGui.QPainter(self.canvas.pixmap())
        self.canvas.pixmap().fill(Qt.green)
        self.draw_wolf(painter)
        self.draw_sheep(painter)
        self.updateSheepLabel()
        self.update()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ChaseGui(Chase(350, 20, 30))
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
