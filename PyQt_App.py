import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(150, 150, 500, 400)
        self.setWindowTitle('New App')
        self.setWindowIcon(QtGui.QIcon('Lava-Rock.png'))

        extractAction = QtGui.QAction('&Get To THE CHOPPAAH!!', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        openEditor = QtGui.QAction('&Editor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = QtGui.QAction('&Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QtGui.QAction('&Save File', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        
        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)
        
        self.home()

    def home(self):
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(200, 175)

        extractAction = QtGui.QAction(QtGui.QIcon('Blue-Stone-Rock.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolbar = self.addToolBar('Extraction')
        self.toolbar.addAction(extractAction)

        fontChoice = QtGui.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolbar = self.addToolBar('Font')
        self.toolbar.addAction(fontChoice)

        color = QtGui.QColor(0,0,0)
        fontColor = QtGui.QAction('Font bg Color', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolbar.addAction(fontColor)

        

##        extractAction = QtGui.QAction(QtGui.QIcon('Purple-Rock.png'), 'Flee the Scene', self)
##        extractAction.triggered.connect(self.close_application)
##        self.toolbar = self.addToolBar('Extraction')
##        self.toolbar.addAction(extractAction)
##
##        extractAction = QtGui.QAction(QtGui.QIcon('Ice-Rock.png'), 'Flee the Scene', self)
##        extractAction.triggered.connect(self.close_application)
##        self.toolbar = self.addToolBar('Extraction')
##        self.toolbar.addAction(extractAction)
##
##        extractAction = QtGui.QAction(QtGui.QIcon('Moss-Rock.png'), 'Flee the Scene', self)
##        extractAction.triggered.connect(self.close_application)
##        self.toolbar = self.addToolBar('Extraction')
##        self.toolbar.addAction(extractAction)

        checkBox = QtGui.QCheckBox('Enlarge Me!', self)
        checkBox.move(300, 30)
        #checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QtGui.QPushButton('Download', self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        #print(self.style().objectName())
        self.styleChoice = QtGui.QLabel('Windows', self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('windowsvista')

        comboBox.move(50, 250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)

        cal = QtGui.QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)
        
        self.show()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')
        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)


    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget { background-color: %s}' % color.name())

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(150, 150, 1000, 800)
        else:
            self.setGeometry(150, 150, 500, 400)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            'Get to the chooppaahh?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print('Extracting NNNoOOOWWWW!!!')
            sys.exit()
        else:
            pass


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
