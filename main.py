#
# MIT License
#
# Copyright (c) 2023 Erriez
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Source: https://github.com/Erriez/pyside6-getting-started
#

from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
from PySide6.QtGui import QAction, QIcon
import os
import sys

# When packaged to a single file with PyInstaller, running the .exe will unpack
# everything to a folder in your TEMP directory, run the script, then discard
# the temporary files. The path of the temporary folder changes with each
# running, but a reference to its location is added to sys as sys._MEIPASS.
# try:
#    os.chdir(sys._MEIPASS)
#    print('Using ' + sys._MEIPASS)
#except:
#    pass


# Find images with Nuitka build option "--include-data-dir=images=images"
def resource_path(filename):
    # Get the absolute path of the directory containing the executable
    exe_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the image file
    image_path = os.path.join(exe_dir, filename)

    # Return the image path
    return image_path


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Resize window
        self.resize(400, 300)
        # Set window title
        self.setWindowTitle('Pyside6 App')
        # Set window icon
        self.setWindowIcon(QIcon(resource_path(r'images/app.png')))

        # Create textbox
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # Create menubar
        file_open = QAction(QIcon(resource_path(r'images/open.png')), 'Open', self)
        file_open.setShortcut('Ctrl+O')
        file_open.setStatusTip('Open new File')
        file_open.triggered.connect(self.show_dialog)

        file_exit = QAction(QIcon(resource_path(r'images/exit.png')), '&Exit', self)
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('Exit application')
        file_exit.triggered.connect(self.close)

        menubar = self.menuBar()
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(file_open)
        menu_file.addSeparator()
        menu_file.addAction(file_exit)
        
        # Create toolbar with Exit button
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(file_open)
        self.toolbar.addAction(file_exit)

        # Create statusbar
        self.statusBar().showMessage('Click File | Open to read a file')

    def show_dialog(self):
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QFontDialog.html
        path, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if not path:
            self.statusBar().showMessage('No file selected'.format())
        elif not os.path.exists(path):
            self.statusBar().showMessage('File {} not found'.format(path))
        else:
            try:
                with open(path, 'r') as f:
                    data = f.read()
                    self.textEdit.setText(data)
                    self.statusBar().showMessage('File {} opened'.format(path))
            except OSError as err:
                self.statusBar().showMessage(err)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

