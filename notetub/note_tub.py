
import sys
from PyQt5.QtWidgets import QApplication
import resources

import os

from notetub.gui import mainwindow, configwidget
from notetub.config import Config



ROOT = os.path.join(os.path.dirname(__file__))
CSS_STYLE = os.path.join(ROOT, "css/style.css")

cfg_path = os.path.join(ROOT, "etc/cfg.yaml")

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(open(CSS_STYLE, "r").read())

    cfg = Config(cfg_path)
    cfg.load_cfg()


    note = mainwindow.MainWindow(cfg=cfg)
    controller = mainwindow.Controller(note)
    note.set_controller(controller)
    note.register_controllers()

    config_manager = configwidget.ConfigManager(cfg)
    note.set_config_manager(config_manager)




    note.show()
    print(note.wizard.frameGeometry())
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()




