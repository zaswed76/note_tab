
import PyQt5
import sys


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

class ConfigLabel(QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)




class Combo(QComboBox):
    def __init__(self):
        super().__init__()

class SliderPrefix(QFrame):
    def __init__(self, *__args):
        super().__init__(*__args)
        vbox = QVBoxLayout(self)
        self.jaro_prefix = QSlider(Qt.Horizontal)

        self.jaro_prefix.setTickPosition(QSlider.TicksBothSides)
        self.jaro_prefix.setMinimum(0)
        self.jaro_prefix.setMaximum(100)
        self.jaro_prefix.setTickInterval(20)
        # self.jaro_prefix.setSingleStep(0.1)
        self.jaro_prefix.setValue(20)

        vbox.addWidget(ConfigLabel("jaro_prefix"))
        vbox.addWidget(self.jaro_prefix)

    def prefix(self):
        return self.jaro_prefix.value()/100




class QSpin(QSpinBox):
    def __init__(self):
        super().__init__()
        self.setMaximum(10000)

class AbcCfgWidget(QLabel):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(name)
        self.setStyleSheet("background-color: #CCCCCE")

class RadioButton(QRadioButton):
    def __init__(self, *__args):
        super().__init__(*__args)

class Algorithms(QGroupBox):
    def __init__(self, *__args):
        """

        :param __args:
        """
        super().__init__(*__args)
        self.algorithms = {}
        self.box = QVBoxLayout()
        self.setLayout(self.box)

    def add_algorithm(self, name):
        self.algorithms[name] = RadioButton(name)
        self.box.addWidget(self.algorithms[name])



    def set_active_algorithm(self, name):
        self.algorithms[name].setChecked(True)

    def get_active_algorithm(self):
        for n, r in self.algorithms.items():
            if r.isChecked():
                return n

class AlgorithmsOptions(QGroupBox):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.options = {}
        self.box = QVBoxLayout()
        self.setLayout(self.box)

    def add_jaro_prefix(self):
        self.slider = SliderPrefix()
        self.box.addWidget(self.slider)





class SearchCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.cfg = cfg
        self.main_box = QVBoxLayout(self)
        self.__init_algorithms()
        self.__init_options()
        self.main_box.addStretch(1)

    def __init_options(self):
        self.algorithm_options = AlgorithmsOptions("опции")
        self.algorithm_options.add_jaro_prefix()
        self.main_box.addWidget(self.algorithm_options)


    def __init_algorithms(self):
        self.algorithm_box = Algorithms("алгоритмы")
        self.main_box.addWidget(self.algorithm_box)
        for alg in self.cfg["algorithm_list"]:
            self.algorithm_box.add_algorithm(alg)


        self.algorithm_box.set_active_algorithm(self.cfg["search_algorithm"])

class LightingCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.cfg = cfg
        box = QVBoxLayout(self)
        box.addLayout(self.symbol_light())
        box.addStretch(1)


    def symbol_light(self):
        box = QHBoxLayout()
        lab = ConfigLabel("выделить n первых символов")
        self.nsymb = QSpin()
        self.nsymb.setValue(self.cfg["ndigits"])
        box.addWidget(lab)
        box.addStretch(1)
        box.addWidget(self.nsymb)

        return box











class TableCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.box_grid = QGridLayout(self)
        self.all_words = QSpin()

        self.all_words.setValue(cfg["max_words"])
        self.box_grid.addWidget(ConfigLabel("найденных слов"), 0, 0)
        self.box_grid.addWidget(self.all_words, 0, 1)


        self.words_on_page = QSpin()
        self.words_on_page.setValue(cfg["words_on_page"])
        self.box_grid.addWidget(ConfigLabel("слов на странице"), 1, 0)
        self.box_grid.addWidget(self.words_on_page, 1, 1)


        self.columns = QSpin()
        self.columns.setValue(cfg["number_columns"])
        self.box_grid.addWidget(ConfigLabel("колонок"), 2, 0)
        self.box_grid.addWidget(self.columns, 2, 1)



        self.box_grid.setRowStretch(3, 1)

class ExFontLabel(QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

class GroupFrame(QFrame):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.box = QHBoxLayout(self)
        self.box.setSpacing(12)

class BorderStyleCombo(GroupFrame):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.cfg = cfg

        lb = ConfigLabel("border style ")
        self.box.addWidget(lb)
        self.box.addWidget(self.combo_box())
        self.box.addStretch(1)


    def combo_box(self):
        self.combo_style = QComboBox()
        styles = self.cfg["border_styles"]
        self.combo_style.addItems(styles)
        self.combo_style.setCurrentText(self.cfg["list_app"]["list_border_style"])
        return self.combo_style

    def current_text(self):
        return self.combo_style.currentText()


class BorderListWidth(GroupFrame):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.cfg = cfg

        self.setFixedHeight(40)
        # self.setStyleSheet("background-color: red")
        lb = ConfigLabel("border width")
        self.box.addWidget(lb)
        self.box.addWidget(self.spin_box())
        self.box.addStretch(1)

    def spin_box(self):
        self.border_width = QSpin()
        self.border_width.setValue(self.cfg["list_app"]["list_border_width"])
        return self.border_width

    def value(self):
        return self.border_width.value()




class ExColorButton(QPushButton):
    def __init__(self, *__args, object_name=None, opt_color=None):
        super().__init__(*__args)
        self.opt_color = opt_color
        self.setObjectName(object_name)
        self.setFixedSize(20, 20)
        self.setCursor(QtCore.Qt.PointingHandCursor)

    def set_color(self, color):
        self.setStyleSheet("""QPushButton {{background-color:{}}}""".format(color))

class ChooseDialogBtn(QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedSize(50, 20)
        self.setCursor(QtCore.Qt.PointingHandCursor)

class FontLabelConf(QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)




class FontConfig(QGroupBox):
    def __init__(self, *__args, font_cfg=None):
        super().__init__(*__args)
        self.font_family = font_cfg["font_family"]
        self.font_size = font_cfg["font_size"]
        self.color = font_cfg["color"]


        self.box = QVBoxLayout()
        self.setLayout(self.box)

        self.box.addLayout(self.font_box())
        self.box.addLayout(self.color_box())




    def show_font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font_family = font.family()
            self.font_size = font.pointSize()
            self.lb.setFont(font)
            self.font_lab_family.setText(str(self.font_family))
            self.font_lab_size.setText(str(self.font_size))



    def show_color_dialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.color = col.name()
            self.color_lb.set_color(self.color)
            self.lb.setStyleSheet("""QLabel {{color:{}}}""".format(self.color))


    def font_box(self):
        box = QHBoxLayout()
        btn = ChooseDialogBtn("шрифт")
        btn.clicked.connect(self.show_font_dialog)
        self.lb = QLabel("пример")
        self.lb.setStyleSheet("""QLabel {{color:{}}}""".format(self.color))
        qfont = QFont()
        qfont.setFamily(self.font_family)
        qfont.setPointSize(self.font_size)
        self.lb.setFont(qfont)
        box.addWidget(btn)
        box.addWidget(self.lb)
        self.font_lab_family = FontLabelConf(str(self.font_family))
        self.font_lab_size = FontLabelConf(str(self.font_size))
        box.addWidget(self.font_lab_family)
        box.addWidget(self.font_lab_size)
        box.addStretch(1)
        return box

    def color_box(self):
        box = QHBoxLayout()
        btn = ChooseDialogBtn("цвет")
        btn.clicked.connect(self.show_color_dialog)
        self.color_lb = ExColorButton()
        self.color_lb.clicked.connect(self.show_color_dialog)
        self.color_lb.set_color(self.color)
        box.addWidget(btn)
        box.addWidget(self.color_lb)
        box.addStretch(1)
        return box


class TableApp(QGroupBox):
    def __init__(self, *__args, cfg=None):
        super().__init__(*__args)
        self.cfg = cfg
        self._bg_color = cfg["list_app"]["list_bg_color"]
        self._border_color = cfg["list_app"]["list_border_color"]
        self.box = QVBoxLayout()
        self.setLayout(self.box)

        self.border_color_btn = self.color_box("border", self.border_color, "set_border_color")
        self.box.addLayout(self.border_color_btn)

        self.bg_color_btn = self.color_box("фон", self.bg_color, "set_bg_color")
        self.box.addLayout(self.bg_color_btn)

        self.border_width = BorderListWidth(cfg)
        self.box.addWidget(self.border_width)


        self.border_style = BorderStyleCombo(cfg)

        self.box.addWidget(self.border_style)


    @property
    def bg_color(self):
        return self._bg_color


    def set_bg_color(self, color):
        self._bg_color = color

    @property
    def border_color(self):
        return self._border_color

    def set_border_color(self, color):
        self._border_color = color

    def show_color_dialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.color = col.name()
            sender = self.sender()
            sender.setStyleSheet("""QPushButton {{background-color:{}}}""".format(self.color))
            getattr(self, sender.opt_color)(self.color)


    def color_box(self, name, color, opt_color):
        box = QHBoxLayout()
        choose_dialog_btn = ChooseDialogBtn(name)

        color_lb = ExColorButton(opt_color=opt_color)
        color_lb.clicked.connect(self.show_color_dialog)
        color_lb.set_color(color)
        box.addWidget(choose_dialog_btn)
        box.addWidget(color_lb)
        box.addStretch(1)
        return box

    def border_size_box(self, name):
        box = QHBoxLayout()
        btn = ChooseDialogBtn(name)
        # btn.clicked.connect(self.show_color_dialog)
        self.color_lb = ExColorButton()
        # self.color_lb.set_color(self.color)
        box.addWidget(btn)
        box.addWidget(self.color_lb)
        box.addStretch(1)
        return box

class ViewCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.cfg = cfg
        self.box = QVBoxLayout(self)

        base_font_cfg = cfg["text_label"]["base"]

        self.base_font = FontConfig("основной шрифт", font_cfg=base_font_cfg)

        pigment_font_cfg = cfg["text_label"]["pigment"]
        self.backlight_font = FontConfig("шрифт подсветки", font_cfg=pigment_font_cfg)

        self.table_app = TableApp("таблица", None, cfg=cfg)


        self.box.addWidget(self.base_font)
        self.box.addWidget(self.backlight_font)
        self.box.addWidget(self.table_app)


class CheckDict(QCheckBox):
    def __init__(self, *__args):
        super().__init__(*__args)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())