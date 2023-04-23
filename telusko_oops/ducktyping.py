class Pycharm:
    def execute(self):
        print("compiling")
        print("running")

class MyEditor:
    def execute(self):
        print("spell checking")
        print("convention checking")
        print("compiling")
        print("running")


class Laptop:
    def code(self,ide):
        ide.execute()

cdk = Pycharm()
sdk = MyEditor()

lap1 = Laptop()
lap1.code(cdk)

