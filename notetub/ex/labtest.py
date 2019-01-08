

#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore



class LWidget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        self.resize(500, 500)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = LWidget()
    txt = """<p style="font-family:'Arial';font-size:20px;color:red">кар<span style="font-family: 'Helvetica';font-size:25px;color:#636363">тошка</span><span style="font-family: 'Helvetica';font-size:20px;color:#636363">ddd</span></p>"""
    main.setText(txt)
    main.show()
    sys.exit(app.exec_())