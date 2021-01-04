import vowels_design
from PyQt5 import QtWidgets
import sys
import os
from loguru import logger

VOWELS = 'аяэеёиыуюо'
convert = {'я': 'а', 'е': 'э', 'ю': 'у', 'ё': 'о', 'и': 'ы'}
CONSONNANTS = 'цкнгшщзхфвпрлджчсмтб'


class Vowels(QtWidgets.QMainWindow, vowels_design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = ''
        self.filename = ""
        self.BtnOpen.clicked.connect(self.open_file)
        self.BtnSave.clicked.connect(self.save_file)

    def open_file(self):
        openfilename = QtWidgets.QFileDialog.getOpenFileName(self, 'open_file', "")[0]
        if openfilename:
            try:
                self.data = open(openfilename, encoding='utf-8')
                self.TxtVowel.clear()
                self.TxtConsonant.clear()
                self.filename = os.path.split(openfilename)[1]
                for ch in self.data.read().lower():
                    if ch in VOWELS:
                        if ch in convert.keys():
                            self.TxtVowel.insertPlainText(convert[ch])
                        else:
                            self.TxtVowel.insertPlainText(ch)
                    if ch in CONSONNANTS:
                        self.TxtConsonant.insertPlainText(ch)
                    if ch == '\n':
                        self.TxtConsonant.insertPlainText(ch)
                        self.TxtVowel.insertPlainText(ch)

            except (UnicodeDecodeError, FileNotFoundError):
                error_message("Ошибка с файлом")

    def save_file(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder:
            [root, ext] = os.path.splitext(self.filename)
            with open(os.path.join(folder, root + '_vow' + ext), 'w') as f:
                f.write(self.TxtVowel.toPlainText())
            with open(os.path.join(folder, root + '_cons' + ext), 'w') as g:
                g.write(self.TxtConsonant.toPlainText())


def error_message(text):
    error = QtWidgets.QMessageBox()
    error.setIcon(QtWidgets.QMessageBox.Critical)
    error.setText(text)
    error.setWindowTitle('Error')
    error.setStandardButtons(QtWidgets.QMessageBox.Ok)
    error.exec_()


def initiate_exception_logging():
    # generating our hook
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        logger.exception(f"{exctype}, {value}, {traceback}")
        # Call the normal Exception hook after
        # noinspection PyProtectedMember
        sys._excepthook(exctype, value, traceback)
        # sys.exit(1)

    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook


@logger.catch
def main():
    initiate_exception_logging()
    app = QtWidgets.QApplication(sys.argv)
    window = Vowels()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
