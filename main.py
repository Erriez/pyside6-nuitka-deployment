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
# Source: https://github.com/Erriez/pyside6-nuitka-deployment
#

from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox
from PySide6.QtGui import QAction, QIcon
import PySide6
import os
import sys
import webbrowser

APP_NAME = 'PySide6 Example'
APP_WEBSITE = 'https://github.com/Erriez/pyside6-nuitka-deployment'
APP_DEVELOPER = 'Erriez'
APP_YEAR = 2023
APP_LICENSE = 'MIT'

# When packaged to a single file with PyInstaller, running the .exe will unpack
# everything to a folder in your TEMP directory, run the script, then discard
# the temporary files. The path of the temporary folder changes with each
# running, but a reference to its location is added to sys as sys._MEIPASS.
try:
    os.chdir(sys._MEIPASS)
    print('Using ' + sys._MEIPASS)
except:
    pass


# Find images with Nuitka build option "--include-data-dir=src=dst"
def resource_path(filename):
    # Get the absolute path of the directory containing the executable
    exe_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the dst file
    dst_path = os.path.join(exe_dir, filename)

    # Return the image path
    return dst_path


def get_app_version():
    app_version = 'Unknown'
    version_file = resource_path(r'data/version.txt')
    if version_file:
        try:
            with open(version_file, 'r') as f:
                app_version = f.readline()
        except OSError:
            pass
    return app_version


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Resize window
        self.resize(400, 300)
        # Set window title
        self.setWindowTitle(APP_NAME)
        # Set window icon
        self.setWindowIcon(QIcon(resource_path(r'images/app.png')))

        # Create textbox
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # Create menubar
        menubar = self.menuBar()

        file_open_action = QAction(QIcon(resource_path(r'images/open.png')), 'Open', self)
        file_open_action.setShortcut('Ctrl+O')
        file_open_action.setStatusTip('Open new File')
        file_open_action.triggered.connect(self.show_dialog)

        file_exit_action = QAction(QIcon(resource_path(r'images/exit.png')), '&Exit', self)
        file_exit_action.setShortcut('Ctrl+Q')
        file_exit_action.setStatusTip('Exit application')
        file_exit_action.triggered.connect(self.close)

        menu_file = menubar.addMenu('&File')
        menu_file.addAction(file_open_action)
        menu_file.addSeparator()
        menu_file.addAction(file_exit_action)

        help_action = QAction(QIcon(resource_path(r'images/web.png')), '&Source on Github', self)
        help_action.setShortcut('F1')
        help_action.setStatusTip('Open Github project website')
        help_action.triggered.connect(self.help)

        about_action = QAction(QIcon(resource_path(r'images/question.png')), '&About', self)
        about_action.setShortcut('Ctrl+?')
        about_action.setStatusTip('About application')
        about_action.triggered.connect(self.about)

        menu_help = menubar.addMenu('&Help')
        menu_help.addAction(help_action)
        menu_help.addSeparator()
        menu_help.addAction(about_action)

        # Create toolbar with Exit button
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(file_open_action)
        self.toolbar.addAction(file_exit_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(help_action)

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

    def help(self):
        webbrowser.open(APP_WEBSITE)

    def about(self, _):
        title = 'About'
        text = f'Application:  {APP_NAME}\n' \
               f'Version:  {get_app_version()}\n' \
               f'Python:  v{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}\n' \
               f'PySide:  v{PySide6.__version__}\n' \
               f'Copyright:  © {APP_YEAR} by {APP_DEVELOPER}\n' \
               f'License:  {APP_LICENSE}'
        QMessageBox.about(self, title, text)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
