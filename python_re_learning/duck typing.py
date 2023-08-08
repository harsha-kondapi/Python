class Pycharm:
    def execute(self):
        print("compiling")
        print("executing")

class MyEditor:
    def execute(self):
        print("spell check")
        print("conventional check")
        print("compiling")
        print("executing")

class Laptop():
    def code(self,ide):
        ide.execute()

#ide = Pycharm()
ide = MyEditor()

lap = Laptop()
lap.code(ide)