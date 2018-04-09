
import npyscreen

class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Hello Habr!")

class MainForm(npyscreen.ActionForm):
    # Конструктор
    def create(self):
        # Добавляем виджет TitleText на форму
        self.title = self.add(npyscreen.TitleText, name="TitleText", value="Hello World!")
    # переопределенный метод, срабатывающий при нажатии на кнопку «ok»
    def on_ok(self):
        self.parentApp.setNextForm(None)
    # переопределенный метод, срабатывающий при нажатии на кнопку «cancel»
    def on_cancel(self):
        self.title.value = "Hello World!"

MyApp = App()
MyApp.run()