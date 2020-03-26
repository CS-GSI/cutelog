from qtpy.QtCore import QFile

name = "settings_dialog.ui"
file = QFile(name)
print(name)
print(file.exists())

filename = 'ui/{}'.format(name)
file = QFile(filename)
print(filename)
print(file.exists())