from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtGui
import os
import sys

# Main window class    
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()  # create layout 
        self.editor = QPlainTextEdit()  # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)


        # Setup the QTextEdit editor configuration 
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont) # Set fonts
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)
        
        # Set the resolution takes four arguments xpos ,ypos, height and width
        self.setGeometry(100, 100, 600, 400)

        # Code for dark ui 
        default_palette = QPalette()
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(dark_palette)


        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

        # adds editor to layout
        layout.addWidget(self.editor)
        
        # Creating a widget layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Sets statusbar object
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # Sets toolbar object
        file_toolbar = QToolBar("File")

        # set the size of toolbar icons
        file_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(file_toolbar)

        # creates a file menu
        file_menu = self.menuBar().addMenu("&File")

        #Adds icons and alternate texts and basic notepad functions
        
        # setStatusTip function is used to provide a tip or a text based discription
        # QAction(QIcon()) is for loading images from directory 
        
        # Toolbar action        
        open_file_action = QAction(QIcon(os.path.join('images', 'blue-folder-open-document.png')), "Open file...", self)
        open_file_action.setStatusTip("Open file")
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)

        # Save action
        save_file_action = QAction(QIcon(os.path.join('images', 'disk.png')), "Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        saveas_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save As...", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)

        # Print action
        print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)

        # creating another tool bar for editing text
        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Edit")

        # undo action
        undo_action = QAction(QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.editor.undo)
        edit_menu.addAction(undo_action)

        # redo action
        redo_action = QAction(QIcon(os.path.join('images', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        # cut action
        cut_action = QAction(QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)

        # copy action
        copy_action = QAction(QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)

        # paste action
        paste_action = QAction(QIcon(os.path.join('images', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)

        # Select action
        select_action = QAction(QIcon(os.path.join('images', 'selection-input.png')), "Select all", self)
        select_action.setStatusTip("Select all text")

        # select all
        select_action.triggered.connect(self.editor.selectAll)
        
        # Adds to toolbar menu
        edit_menu.addAction(select_action)
        edit_menu.addSeparator()

        # Wrap action
        wrap_action = QAction(QIcon(os.path.join('images', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.setStatusTip("Toggle wrap text to window")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(wrap_action)

        # calls update title method
        self.update_title()
        
        # shwoing all components
        self.show()

    #show errors
    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

#File operations
    # open action 
    def file_open(self):
        # Gets bool value and path
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            # If we do not have a path, we need to use Save As.
            return self.file_saveas()

        self._save_to_path(self.path)

        
    # Action for save function
    
    def file_saveas(self):
        # opening path or extension 
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files(*.*)")

        if not path:
            # If dialog is cancelled, will return ''
            return

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        # Handle the exceptions
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))
            
        # updates the title
        else:
            self.path = path
            self.update_title()

    def file_print(self):

        # creating a QPrintDialog
        dlg = QPrintDialog()
        
        # if executed
        if dlg.exec_():
            # print the text
            self.editor.print_(dlg.printer())

    # Update title method
    def update_title(self):
        # set title with prefix
        self.setWindowTitle("%s - Py_Notepad" % (os.path.basename(self.path) if self.path else "Untitled"))

    # Action called by edit toggle
    def edit_toggle_wrap(self):
        # changing line wrap mode
        self.editor.setLineWrapMode( 1 if self.editor.lineWrapMode() == 0 else 0 )

    # Toggle theme function
    def toggleDarkTheme(self):
        if not togglePushButton.isChecked():
            self.setPalette(palette)
        else:
            self.setPalette(default_palette)
            
# drivers code 
if __name__ == '__main__':

    # create an Qt application
    app = QApplication(sys.argv)
    
    # set the theme
    app.setStyle('Fusion') #Style needed for palette to work

    # sets the name of application
    app.setApplicationName("Py_Notepad")

    # setting window icon
    app.setWindowIcon(QtGui.QIcon(os.path.join('images', 'icon.png')))

    # creating main windows object
    window = MainWindow()

    #loop the window
    app.exec_()

#Fix toggle  shit
### Toggle push button
##togglePushButton = QPushButton("Dark Mode")
##togglePushButton.setCheckable(True)
##togglePushButton.setChecked(True)
##togglePushButton.clicked.connect(toggleDarkTheme)
##layout.addWidget(togglePushButton,2,3)
