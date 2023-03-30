import sys
import cv2
import numpy
from matplotlib import pyplot
from skimage.measure import block_reduce
from PyQt5 import QtCore, QtGui, QtWidgets
chart = []

class Ui_Interface(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 122)
        MainWindow.setMinimumSize(QtCore.QSize(700, 300))
        MainWindow.setMaximumSize(QtCore.QSize(700, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 50, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 50, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 100, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 100, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 180, 300, 70))
        self.pushButton_2.clicked.connect(self.result_view)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Количество эталонов"))
        self.label_3.setText(_translate("MainWindow", "Количество классов"))
        self.pushButton_2.setText(_translate("MainWindow", "Вывод результата"))

    def result_view(self):
        results = end_results()
        m = int(self.lineEdit_2.text())
        pyplot.ion()
        fig = pyplot.figure(figsize=(5, 10))
        fig.patch.set_facecolor('skyblue')

        for i in range(m):
            pyplot.clf()

            img = pyplot.subplot(3, 2, 1)
            hist = pyplot.subplot(3, 2, 2)
            gradient = pyplot.subplot(3, 2, 3)
            dft = pyplot.subplot(3, 2, 4)
            dct = pyplot.subplot(3, 2, 5)
            scale = pyplot.subplot(3, 2, 6)

            img.imshow(image_type(i, 0, 'img_first'))
            img.set_xticks([])
            img.set_yticks([])
            img.set_xlabel('ИЗОБРАЖЕНИЕ ' + str(i + 1))

            hist.imshow(image_type(results[0][i] - 1, 0, 'img_first'))
            hist.set_xticks([])
            hist.set_yticks([])
            hist.set_xlabel('Гистограмма яркости' + '\n КЛАСС  ' + str(results[0][i]))

            gradient.imshow(image_type(results[1][i] - 1, 0, 'img_first'))
            gradient.set_xticks([])
            gradient.set_yticks([])
            gradient.set_xlabel('Градиент' + '\n КЛАСС  ' + str(results[1][i]))

            dft.imshow(image_type(results[2][i] - 1, 0, 'img_first'))
            dft.set_xticks([])
            dft.set_yticks([])
            dft.set_xlabel('DFT' + '\n КЛАСС ' + str(results[2][i]))

            dct.imshow(image_type(results[3][i] - 1, 0, 'img_first'))
            dct.set_xticks([])
            dct.set_yticks([])
            dct.set_xlabel('DCT' + '\n КЛАСС ' + str(results[3][i]))

            scale.imshow(image_type(results[4][i] - 1, 0, 'img_first'))
            scale.set_xticks([])
            scale.set_yticks([])
            scale.set_xlabel('Scale' + '\n КЛАСС ' + str(results[4][i]))

            pyplot.draw()
            pyplot.pause(2)

        pyplot.ioff()
        pyplot.show()
        results = end_results()
        ln = len(results)
        chart = [[] for x in range(ln)]
        m = int(self.lineEdit_2.text())

        for i in range(ln):
            quantity = 0
            count = 0

            for j in range(len(results[0])):
                count = count + 1
                if results[i][j] == j + 1:
                    quantity += 1

                chart[i].append(quantity / count * 100)

        fig = pyplot.figure(figsize=(10, 10))
        fig.patch.set_facecolor('skyblue')

        hist = pyplot.subplot(3, 2, 1)
        gradient = pyplot.subplot(3, 2, 2)
        dft = pyplot.subplot(3, 2, 3)
        dct = pyplot.subplot(3, 2, 4)
        scale = pyplot.subplot(3, 2, 5)

        hist.plot(numpy.arange(m), chart[0], 'orange', linewidth=5)
        hist.set_xlabel('Гистаграмма яркости')
        hist.set_facecolor('CadetBlue')
        gradient.plot(numpy.arange(m), chart[1], 'orange', linewidth=5)
        gradient.set_xlabel('Градиент')
        gradient.set_facecolor('CadetBlue')
        dft.plot(numpy.arange(m), chart[2], 'orange', linewidth=5)
        dft.set_xlabel('DFT')
        dft.set_facecolor('CadetBlue')
        dct.plot(numpy.arange(m), chart[3], 'orange', linewidth=5)
        dct.set_xlabel('DCT')
        dct.set_facecolor('CadetBlue')
        scale.plot(numpy.arange(m), chart[4], 'orange', linewidth=5)
        scale.set_xlabel('Scale')
        scale.set_facecolor('CadetBlue')
        pyplot.show()

def image_type(i, j, type_):
    img_first = cv2.imread('ORL_Faces/s' + str(i + 1) + '/' + str(j + 1) + '.pgm')
    img_second = cv2.imread('ORL_Faces/s' + str(i + 1) + '/' + str(j + 1) + '.pgm', 0)

    if type_ == 'img_first':
        return img_first

    if type_ == 'img_second':
        return img_second

    if type_ == 'img_gr':
        return cv2.cvtColor(img_first, cv2.COLOR_BGR2GRAY)

    if type_ == 'img_fl':
        return numpy.float32(img_second)


def method_selection(x, y, type_):
    if type_ == 1:
        img_result = image_type(x, y, 'img_first')
        return numpy.histogram(img_result.ravel(), 256, [0, 256])

    if type_ == 2:
        img_result = image_type(x, y, 'img_second')
        return numpy.uint8(numpy.absolute(cv2.Laplacian(img_result, cv2.CV_64F, ksize=5)))

    if type_ == 3:
        img_result = image_type(x, y, 'img_gr')
        return numpy.log(numpy.abs(numpy.fft.fftshift(numpy.fft.fft2(img_result))))

    if type_ == 4:
        img_result = image_type(x, y, 'img_fl')
        return numpy.uint8(cv2.dct(img_result, cv2.DCT_ROWS))

    if type_ == 5:
        img_result = image_type(x, y, 'img_second')
        return numpy.array(block_reduce(img_result, (2, 1), numpy.max))

def distance_search(count_standarts, count_images, type_):
    results = []
    templates = []

    for i in range(count_images):
        results.append([])
        templates.append([])

    for i in range(count_images):
        method = method_selection(i, count_standarts, type_)[0]
        histogram = numpy.zeros(method.shape)
        for j in range(count_standarts):
            histogram = histogram + method
        templates[i] = histogram / count_standarts

    for i in range(count_images):
        for j in range(count_images):
            distance_vector = 0.0
            for k in range(count_standarts, 10):
                method = method_selection(j, k, type_)[0]
                histogram = method
                for l in range(len(method)):
                    distance_vector = distance_vector + (templates[i][l] - histogram[l]) ** 2
            distance_vector = distance_vector / (10 - count_standarts)
            results[i].append(distance_vector)
        if numpy.argmin(results[i]) == i:
            results[i] = i + 1
        else:
            results[i] = numpy.argmin(results[i]) + 1

    return results

def end_results():
    n = int(ui.lineEdit.text())
    m = int(ui.lineEdit_2.text())
    results = []
    for i in range(5):
        results.append(distance_search(n, m, i + 1))
    return results

app = QtWidgets.QApplication(sys.argv)
Interface = QtWidgets.QMainWindow()
ui = Ui_Interface()
ui.setupUi(Interface)
Interface.show()
sys.exit(app.exec_())
