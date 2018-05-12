class MyApp:
    def myFunc_1(self):
        print('i am myFunc_1')

    def myFunc_2(self):
        print('i am myFunc_2')

    def run(self):
        for i in range(1, 3):
            rb = 'myFunc_' + str(i)
            getattr(self, rb)()


if __name__ == '__main__':
    MyApp().run()