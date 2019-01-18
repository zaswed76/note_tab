
import sys
from PyQt5.QtWidgets import QApplication


import os

from notetub.gui import mainwindow, configmanager
from notetub.config import Config

from notetub import resources


ROOT = os.path.join(os.path.dirname(__file__))
CSS_STYLE = os.path.join(ROOT, "css/style.css")
print(ROOT, "!!!!!!!!!!!!!!!")

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

    config_manager = configmanager.ConfigManager(note, cfg)
    note.set_config_manager(config_manager)




    note.show()

    sys.exit(app.exec_())




if __name__ == '__main__':
    main()




