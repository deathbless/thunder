import sys
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QFileDialog, QDialog, QApplication, QWidget,\
    QPushButton, QLabel, QLineEdit, QHBoxLayout, QFormLayout
from PyQt4.QtCore import QDir

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        #self.le = QLabel()
        self.le = QLineEdit()
        self.le.setObjectName("Empty")
        self.le.setText("Empty")

        self.pb = QPushButton()
        self.pb.setObjectName("browse")
        self.pb.setText("Browse") 

        layout = QHBoxLayout()
        layout.addWidget(self.le)
        layout.addWidget(self.pb)

        self.setLayout(layout)
        self.connect(self.pb, SIGNAL("clicked()"), self.button_click)
        self.setWindowTitle("Learning")

    def button_click(self):
        # absolute_path is a QString object
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file', '.', "All files (*.*)")
        if absolute_path:
            cur_path = QDir('.')
            relative_path = cur_path.relativeFilePath(absolute_path)
            self.le.setText(absolute_path)
        
            print relative_path

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
