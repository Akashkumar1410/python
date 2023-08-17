import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QTextCursor, QKeySequence
from PyQt5.QtCore import Qt

class NotepadApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()





    def init_ui(self):

        # Set initial window dimensions here
        self.resize(800, 600)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.undo_action = QAction('Undo', self)
        self.undo_action.setShortcut(QKeySequence.Undo)
        self.undo_action.triggered.connect(self.text_edit.undo)

        self.redo_action = QAction('Redo', self)
        self.redo_action.setShortcut(QKeySequence.Redo)
        self.redo_action.triggered.connect(self.text_edit.redo)

        self.cut_action = QAction('Cut', self)
        self.cut_action.setShortcut(QKeySequence.Cut)
        self.cut_action.triggered.connect(self.text_edit.cut)

        self.copy_action = QAction('Copy', self)
        self.copy_action.setShortcut(QKeySequence.Copy)
        self.copy_action.triggered.connect(self.text_edit.copy)

        self.paste_action = QAction('Paste', self)
        self.paste_action.setShortcut(QKeySequence.Paste)
        self.paste_action.triggered.connect(self.text_edit.paste)

        self.save_action = QAction('Save', self)
        self.save_action.setShortcut(QKeySequence.Save)
        self.save_action.triggered.connect(self.save_file)

        self.save_as_action = QAction('Save As...', self)
        self.save_as_action.triggered.connect(self.save_file_as)

        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu('File')
        self.edit_menu = self.menu_bar.addMenu('Edit')

        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)

        self.edit_menu.addAction(self.undo_action)
        self.edit_menu.addAction(self.redo_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)

        self.show()

    def save_file(self):
        if not self.text_edit.toPlainText():
            QMessageBox.warning(self, 'Empty Document', 'Cannot save an empty document.')
            return

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)', options=options)

        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit.toPlainText())

    def save_file_as(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File As', '', 'Text Files (*.txt);;All Files (*)', options=options)

        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit.toPlainText())

def main():
    app = QApplication(sys.argv)
    ex = NotepadApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
